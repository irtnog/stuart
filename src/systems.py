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

import logging

from flask import Blueprint, render_template
from lethbridge.database import System
from lethbridge.schemas.spansh import SystemSchema

from .app import db

# configure module-level logging
logger = logging.getLogger(__name__)

url_prefix = "/".join(__name__.split(".")[1:]).replace("_", "-")
bp = Blueprint(__name__.split(".")[-1], __name__, url_prefix=f"/{url_prefix}")


@bp.route("/")
def index():
    return render_template(f"{url_prefix}/index.html")


@bp.route("/<int:id64>", methods=["GET"])
def get_system_by_id(id64: int):
    return SystemSchema().dump(db.get_or_404(System, id64))
