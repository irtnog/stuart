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

import logging
import pkg_resources
import pkgutil

__app_name__ = __name__
__version__ = pkg_resources.require(__app_name__)[0].version

# configure module-level logging
logger = logging.getLogger(__name__)

# add support for dynamically loading blueprints
__path__ = pkgutil.extend_path(__path__, __name__)  # noqa: F821
