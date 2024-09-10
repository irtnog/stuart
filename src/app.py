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

import importlib
import logging
import pkgutil

from flask import Blueprint, Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from lethbridge.config import DEFAULT_CONFIG
from lethbridge.database import Base

from . import __app_name__, __path__, __version__

# configure module-level logging
logger = logging.getLogger(__name__)

# create Flask extension objects
bootstrap = Bootstrap5()
db = SQLAlchemy(model_class=Base)
talisman = Talisman()


def create_app(test_config=None) -> Flask:
    # create and configure the web app
    app = Flask(__app_name__, instance_relative_config=True)
    app.config.from_mapping(
        BOOTSTRAP_BOOTSWATCH_THEME="cyborg",
        BOOTSTRAP_SERVE_LOCAL=True,
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=DEFAULT_CONFIG["database"]["uri"],
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # load extensions
    bootstrap.init_app(app)
    db.init_app(app)
    talisman.init_app(app)

    # pass functions/variables to Jinja templates; see also
    # flask.Flask.context_processor
    app.jinja_env.globals["stuart_version"] = __version__

    # load blueprints from submodules
    [
        (lambda bp: app.register_blueprint(bp) if isinstance(bp, Blueprint) else None)(
            getattr(module, "bp", None)
        )
        for module in [
            importlib.import_module(modname)
            for importer, modname, ispkg in pkgutil.walk_packages(
                path=__path__,
                prefix=__app_name__ + ".",  # start from parent module
            )
            if modname != __name__  # avoid circular import
        ]
    ]

    return app
