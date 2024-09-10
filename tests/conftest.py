# stuart, a self-hostable game data aggregator for Elite: Dangerous
# Copyright (C) 2023  Matthew X. Economou
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <https://www.gnu.org/licenses/>.

from pathlib import Path
from shutil import copy

import alembic.command
import alembic.config
import simplejson as json
from flask import Flask
from lethbridge.schemas.spansh import SystemSchema
from pytest import TempPathFactory, fixture, mark, param
from pytest_postgresql import factories
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from stuart.app import create_app


def load_database(db_type: str, **kwargs):
    """Prepare a database template for use by multiple tests."""
    match db_type:
        case "postgresql":
            db_uri = (
                f"postgresql+psycopg2://{kwargs['user']}"
                + f":@{kwargs['host']}"
                + f":{kwargs['port']}"
                + f"/{kwargs['dbname']}"
                + "?options=-c timezone=utc"
            )
        case "sqlite":
            db_uri = f"sqlite:///{kwargs['filename']}"

    # Init the database via Alembic.
    alembic_cfg = alembic.config.Config()
    alembic_cfg.set_main_option("script_location", "lethbridge:migrations")
    alembic_cfg.set_main_option("databases", db_type)
    alembic_cfg.set_section_option(db_type, "sqlalchemy.url", db_uri)
    alembic.command.upgrade(alembic_cfg, "head")

    # Use simplejson to read the test data.
    data_file = Path(__file__).parent / "mock-galaxy-data.json"
    load_data = json.loads(data_file.read_text(), use_decimal=True)

    # Load the test data with Marshmallow.
    engine = create_engine(db_uri, poolclass=NullPool)
    for load_datum in load_data:
        try:
            with sessionmaker(engine).begin() as session:
                new_system = SystemSchema().load(load_datum, session=session)
                session.add(new_system)
        except Exception as e:
            # Add the system name/id64 to error message for
            # diagnostics.
            raise (type(e))(f"Loading {load_datum['name']} ({load_datum['id64']}): {e}")


def load_database_postgresql(**kwargs):
    """Prepare a PostgreSQL database template for use by multiple
    tests."""
    load_database("postgresql", **kwargs)


postgresql_proc = factories.postgresql_proc(load=[load_database_postgresql])
postgresql = factories.postgresql("postgresql_proc")


@fixture(scope="session")
def sqlite_proc(tmp_path_factory: TempPathFactory):
    db_file = tmp_path_factory.mktemp("sqlite_proc") / "db.sqlite3"
    db_file.touch()
    load_database("sqlite", filename=db_file)
    yield db_file


@fixture
def sqlite(tmp_path: Path, request):
    sqlite_proc: Path = request.getfixturevalue("sqlite_proc")
    db_file = tmp_path / "db.sqlite3"
    copy(sqlite_proc, db_file)
    yield db_file


# Invoke smoke tests with `pytest -k smoke -x`.  See also
# https://docs.pytest.org/en/stable/mark.html,
# https://stackoverflow.com/a/52369721,
# https://docs.pytest.org/en/stable/how-to/fixtures.html#parametrizing-fixtures,
# https://docs.pytest.org/en/stable/how-to/fixtures.html#using-marks-with-parametrized-fixtures
@fixture(
    params=[
        "postgresql",
        param("sqlite", marks=mark.smoke),
    ],
)
def mock_db_uri(request):
    fixture = request.getfixturevalue(request.param)
    match request.param:
        case "postgresql":
            yield (
                f"postgresql+psycopg2://{fixture.info.user}"
                + f":@{fixture.info.host}"
                + f":{fixture.info.port}"
                + f"/{fixture.info.dbname}"
                + "?options=-c timezone=utc"
            )
        case "sqlite":
            yield f"sqlite:///{fixture}"


@fixture
def app(mock_db_uri) -> Flask:
    test_config = {
        "SQLALCHEMY_DATABASE_URI": mock_db_uri,
    }
    app = create_app(test_config)
    return app
