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

from pytest import mark


@mark.order("first")
def test_app(client):
    response = client.get("/")
    assert 200 <= response.status_code < 400


@mark.order("first")
def test_https_redirect(client):
    response = client.get(
        "/",
        environ_overrides={"wsgi.url_scheme": "http"},
    )
    assert response.status_code == 302
    assert response.location.startswith("https://")


@mark.order("first")
def test_security_headers(client):
    response = client.get(
        "/",
        environ_overrides={"wsgi.url_scheme": "https"},
    )
    assert response.status_code == 200
    for security_header in [
        "X-Content-Type-Options",
        "Content-Security-Policy",
        "Referrer-Policy",
        "Permissions-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
    ]:
        assert security_header in response.headers
