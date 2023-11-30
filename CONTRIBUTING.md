# Contributing

This project uses the [Git feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).  Please submit your changes for review as a [GitHub pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests).

## Development Environment

This project requires Python 3.10 or newer.  To set up your development environment on Linux, run these commands from the project root directory:

- `sudo make build-deps`—installs build dependencies (Debian/Ubuntu only)

- `make`—creates a virtual environment named `.venv` in the current working directory and performs an editable installation of this project, including development and testing tools

- `make pre-commit`—installs pre-commit hooks (requires the virtual environment to be active in your code editor or [Git porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain))

- `make test`—performs comprehensive functional and integration testing of this project

- `make smoke`—runs a shorter, faster subset of the test suite

- `make docker`—builds a fully tested and release-ready container image

Additional [make(1)](https://linux.die.net/man/1/make) targets are available.  Review the [Makefile](Makefile) for details.

## Code Style

The following code styles are in use:

- [Python Black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/)

- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

- [the Home Assistant YAML style guide](https://developers.home-assistant.io/docs/documenting/yaml-style-guide/)

## Commit Messages

This project implements [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) using [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).  Valid commit types are:

- **build**—changes to the build system or external dependencies

- **ci**—changes to the CI configuration files and scripts

- **docs**—documentation-only changes

- **feat**—a new feature

- **fix**—a bug fix

- **perf**—a code change that improves performance

- **refactor**—a code change that neither fixes a bug nor adds a feature

- **test**—new tests or corrections to existing tests

A commit's scope should be the second-level Python module name sans the `stuart.` prefix or any suffixes with a few exceptions.  Valid commit scopes are:

- [stuart](src/__init__.py)—for the corresponding top-level dunder module

- [app](src/app.py)—the web application, using [Flask](https://flask.palletsprojects.com/)

- [main](src/main.py)—the main web page and related routes

- [wsgi](src/wsgi.py)—the [WSGI adapter](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), for use with [gunicorn](https://gunicorn.org/)

- **packaging**—package layout or other metadata, e.g., the arrangement of [src/](src/), alterations to [pyproject.toml](pyproject.toml) or [Dockerfile](Dockerfile)

- no scope—for **refactor** or **test** changes covering multiple packages; or for **build**, **ci**, or **doc** changes not specific to one package
