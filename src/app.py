# stuart, web front end for Elite: Dangerous game data collated by lethbridge
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
from flask_talisman import Talisman

from . import __app_name__, __path__

# configure module-level logging
logger = logging.getLogger(__name__)

# create Flask extension objects
talisman = Talisman()


def create_app(test_config=None) -> Flask:
    # create and configure the web app
    app = Flask(__app_name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py", silent=True)

    # load extensions
    talisman.init_app(app)

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
