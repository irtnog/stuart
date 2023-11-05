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

stuart.egg-info: .venv
	. .venv/bin/activate; pip install -e .[dev,test]

.venv:
	python3 -m venv --system-site-packages $@

debug: stuart.egg-info
	. .venv/bin/activate; python3 -m flask --debug --app stuart.app run

run: debug

test: stuart.egg-info
	. .venv/bin/activate; pytest

coverage: stuart.egg-info
	. .venv/bin/activate; pytest --cov=stuart

clean:
	rm -rf .coverage stuart.egg-info .pytest_cache .venv*
	find . -type d -name __pycache__ -print | xargs rm -rf

container:
	docker build -t stuart .

docker: container
