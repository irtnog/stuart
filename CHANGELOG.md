# CHANGELOG



## v0.1.0 (2023-11-30)

### Build

* build: update classifiers to better reflect this package&#39;s purpose ([`eb2b9c2`](https://github.com/irtnog/stuart/commit/eb2b9c2a29e3df3857cb0de22ec77ee6f68b7a4d))

* build: configure isort to work with Black ([`27f92b9`](https://github.com/irtnog/stuart/commit/27f92b909fde11b8a4cb7d49def71cc1e805e7d5))

* build: force the README to be parsed as Markdown ([`c0ad352`](https://github.com/irtnog/stuart/commit/c0ad352b6f203ca4ae195e176dbc13a6bf247ef9))

* build: add optional dependencies for supported database clients ([`208ac3c`](https://github.com/irtnog/stuart/commit/208ac3cb19e52880ba50d84619ac6a40aefce802))

* build: update the development environment to match Lethbridge ([`6ad80a2`](https://github.com/irtnog/stuart/commit/6ad80a21a3e5e7a4d6cece036087106d3b682400))

* build: add a dependency on the new Lethbridge package ([`976795c`](https://github.com/irtnog/stuart/commit/976795c82d610ea39c9d0c802f6e0d252306d1bb))

* build: require a setuptools that supports editable installs with pyproject ([`ec03ad7`](https://github.com/irtnog/stuart/commit/ec03ad7abbc1ce665c7c1e31e30e044e83c324b7))

* build: keep project sections sorted ([`809d7f9`](https://github.com/irtnog/stuart/commit/809d7f91e5a0c9a6dae7c31593a0372a4d8edc8d))

* build: add import order checking using isort to the pre-commit hooks ([`8384518`](https://github.com/irtnog/stuart/commit/83845186eb7842fd28561ffa78f5b41fd21ce31a))

* build: add flake8 syntax checking to the pre-commit hooks ([`cc56a6e`](https://github.com/irtnog/stuart/commit/cc56a6eecf8e68ee87d76add0b967fe64ad818d3))

* build: upgrade the Black pre-commit hook v23.3.0-&gt;v23.11.0 ([`f39accf`](https://github.com/irtnog/stuart/commit/f39accfb6300fee4865706b737f97f968cd6204a))

* build: upgrade pre-commit-hooks v2.3.0-&gt;v4.5.0 ([`2e58b27`](https://github.com/irtnog/stuart/commit/2e58b273aba929cd4f55d9412cd5608e4d9a42ba))

* build: optimize the container build process by managing the cache better ([`d8be84f`](https://github.com/irtnog/stuart/commit/d8be84fc692f68399bd7eef049f9b592d4726e72))

* build: upgrade container to Python 3.11 ([`f44975a`](https://github.com/irtnog/stuart/commit/f44975a4885a1ec277ecc5c69cd806fec4e89653))

* build: exclude Python bytecode from the container image

This improves Docker build cache management by excluding what are in
effect temporary files from the build context. ([`53dcaec`](https://github.com/irtnog/stuart/commit/53dcaecc2b943c3fe40671b7318f99d2f4416d15))

### Ci

* ci: grant python-semantic-release permission to update the GitHub repo ([`117ac2e`](https://github.com/irtnog/stuart/commit/117ac2e49d0ed9d349181ba093999da893d0ef95))

* ci: automate releases ([`4234625`](https://github.com/irtnog/stuart/commit/42346259f1a4c639a0b54e2ba47341ed2c7a214d))

* ci: run tests after linting ([`de62e92`](https://github.com/irtnog/stuart/commit/de62e926712192c84b8ae688ca24c034e9725876))

* ci: reuse the pre-commit hook ([`368e614`](https://github.com/irtnog/stuart/commit/368e61416b68a14aec0cd499d1f1fcfc602605d1))

### Documentation

* docs: provide developer guidance ([`2e86cc6`](https://github.com/irtnog/stuart/commit/2e86cc62d74c55496b12b546984a425eba926a56))

### Feature

* feat: create a basic Flask app ([`e383374`](https://github.com/irtnog/stuart/commit/e383374dc0b61fba84b2451ae6cce6407f34f9c2))

### Fix

* fix(stuart): migrate from pkg_resources to importlib.metadata

Cf. https://setuptools.pypa.io/en/latest/pkg_resources.html. ([`2589fd5`](https://github.com/irtnog/stuart/commit/2589fd5ae52688f430ba8d4b3c687cd637cfbb02))

* fix: sort imports ([`3d920d5`](https://github.com/irtnog/stuart/commit/3d920d53b3dc743bb7a6331f0e31c0b5eb318569))

### Test

* test: add a marker for slow tests ([`4ff8b52`](https://github.com/irtnog/stuart/commit/4ff8b529985d238b959e16d1d69cedfc40b8f8bc))
