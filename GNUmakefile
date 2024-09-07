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

# Search a colon-separated list of directories for one of the given
# programs, returning the first match.
pathsearch = \
$(or \
	$(firstword \
		$(foreach a, $(2), \
			$(wildcard $(addsuffix /$(a), $(subst :, , $(1)))))), \
	$(3))

# Search the Python virtual environment and the executable search path
# for the programs in the listed order, returning the first match.
venvsearch = \
$(if $(call pathsearch,.venv/bin,$(1)), \
	. .venv/bin/activate; $(1), \
	$(call pathsearch,$(PATH),$(1),exit 1; echo $(1)))

# Develop using the latest available supported version of Python.
PYTHON = \
$(call pathsearch,$(PATH),python3.12 python3.11 python3.10,exit 1; echo python3)
PYTHON_VERSION = \
$(shell $(PYTHON) -c "import sys;print('{}.{}'.format(*sys.version_info[:2]))")

# Use these tools from the development environment, if available.
PRE_COMMIT = $(call venvsearch,pre-commit)
PYTEST	   = $(call venvsearch,pytest)
TOMLQ	   = $(call venvsearch,tomlq)
YQ	   = $(call venvsearch,yq)

# Determine the host operating system.
UNAME       = $(or $(shell uname))
LSB_RELEASE = $(call pathsearch,$(PATH),lsb_release,exit 1; echo lsb_release)
DISTRO      = $(if $(filter Linux, $(UNAME)), $(or $(shell $(LSB_RELEASE) -is)))

# Use these settings when developing on Debian/Ubuntu.
APT_GET = \
	apt-get -o Debug::pkgProblemResolver=yes -y --no-install-recommends
DEBIAN_BUILD_DEPS = \
	build-essential \
	devscripts \
	equivs \
	postgresql \

# Get the package name.
PYPACKAGE_NAME = \
$(shell $(TOMLQ) -r '.tool.setuptools."package-dir"|keys[0]' pyproject.toml)

# List in-use pre-commit hooks.
PRE_COMMIT_HOOKS = \
$(addprefix .git/hooks/, \
	$(shell \
		$(YQ) -r ".repos[].hooks[].stages[]" .pre-commit-config.yaml \
			2>/dev/null \
		| sort -u \
	) \
	pre-commit \
)

# When adding an alias for a build artifact, add it to this list; cf.
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html.
.PHONY: \
	build-deps \
	clean \
	clean-deps \
	coverage \
	debug \
	dist \
	distcheck \
	distclean \
	lint \
	pre-commit \
	run \
	setup \
	smoke \
	test \
	tests \
	venv \

# Debug/run the web app.
debug: .coverage
	. .venv/bin/activate; python -m flask --debug --app stuart.app run $(ARGS)

run: .coverage
	. .venv/bin/activate; python -m flask --app stuart.app run $(ARGS)

# Build the distribution.
dist: .coverage
	. .venv/bin/activate; python -m build

distcheck:
	. .venv/bin/activate; twine check dist/*

distclean:
	rm -rf dist

# Run the test suite.
test tests coverage: .coverage
.coverage: $(PYPACKAGE_NAME).egg-info tests/*.py
	$(PYTEST) --cov=$(PYPACKAGE_NAME) $(PYTEST_ARGS)

smoke: $(PYPACKAGE_NAME).egg-info tests/*.py
	$(PYTEST) -m "smoke and not slow" $(PYTEST_ARGS)

# Run the linter (including unstaged changes).
lint: $(PRE_COMMIT_HOOKS)
	$(PRE_COMMIT) run --show-diff-on-failure --all-files

# Install the pre-commit hooks.
pre-commit: $(PRE_COMMIT_HOOKS)
.git/hooks/%: .pre-commit-config.yaml | setup
	$(PRE_COMMIT) validate-config
	$(PRE_COMMIT) validate-manifest
	$(PRE_COMMIT) install --install-hooks --hook-type $*

# Set up the development environment.
setup: $(PYPACKAGE_NAME).egg-info
$(PYPACKAGE_NAME).egg-info: pyproject.toml src/*.py | venv
	. .venv/bin/activate; python -m pip install -e .[psycopg2cffi,dev,test]
	echo "from psycopg2cffi import compat\ncompat.register()" \
		> .venv/lib/python$(PYTHON_VERSION)/site-packages/psycopg2.py

# Create the development environment.
venv: .venv
.venv:
	$(PYTHON) -m venv $@
	. .venv/bin/activate; python -m pip install -U pip-with-requires-python
	. .venv/bin/activate; python -m pip install -U pip setuptools

# Remove build artifacts and reset the development environment.
clean:
	rm -rf build .coverage dist *.egg-info .pytest_cache .venv* \
		$(PRE_COMMIT_HOOKS)
	find . -type d -name __pycache__ -print | xargs rm -rf

# Install development tools and build dependencies (requires local
# administrator rights).
build-deps:
	$(if $(UNAME), \
		$(if $(filter 0, $(or $(shell id -u))),, \
			@echo You must be root to perform this action.; exit 1))
	$(if $(filter Debian Ubuntu, $(DISTRO)), \
		sed -i '/deb-src/s/^# //' /etc/apt/sources.list \
		&& apt-get update \
		&& (which jq > /dev/null || ($(APT_GET) install jq)) \
		&& (which python3.12 > /dev/null \
			|| (add-apt-repository -y ppa:deadsnakes/ppa \
				&& $(APT_GET) install python3.12-full \
				&& curl https://bootstrap.pypa.io/get-pip.py \
					| python3.12 -)) \
		&& (which mk-build-deps > /dev/null \
			|| ($(APT_GET) install $(DEBIAN_BUILD_DEPS) \
				&& mk-build-deps -i -r -t "$(APT_GET)" \
					python3-psycopg2 \
				&& mk-build-deps -i -r -t "$(APT_GET)" \
					python3-psycopg2cffi \
				&& rm -f *.buildinfo *.changes)))

# This could remove packages other that the ones listed, so keep any
# confirmation prompts (requires local administrator rights).
clean-deps:
	$(if $(UNAME), \
		$(if $(filter 0, $(or $(shell id -u))),, \
			@echo You must be root to perform this action.; exit 1))
	$(if $(filter Debian Ubuntu, $(DISTRO)), \
		apt-mark auto \
			$(DEBIAN_BUILD_DEPS) \
			psycopg2-build-deps \
			python-psycopg2cffi-build-deps \
		&& apt-get autoremove)
