# CHANGELOG

## v0.2.0 (2024-09-10)

### Build

* build: publish dependency pins only on GitHub ([`a6dd599`](https://github.com/irtnog/stuart/commit/a6dd599c0b37d1d85dd2401c837b69335b39b9f3))

* build: redefine phony targets so they can be re-run when invoked directly ([`64730f3`](https://github.com/irtnog/stuart/commit/64730f30fc680910b9377bf9f471bab23f2722b3))

* build: add pip-compile to the development environment ([`a7fec73`](https://github.com/irtnog/stuart/commit/a7fec73e311c6d3de04d07fa858aa59fe7814fa4))

* build: add YAML and TOML processors to the development environment ([`c2f05cb`](https://github.com/irtnog/stuart/commit/c2f05cb3d4689ad8b9f71aa99b1c6b1f3ed05ff7))

* build: remove unused tools from the development environment ([`3298dc7`](https://github.com/irtnog/stuart/commit/3298dc79f1b9f761cd9ae03d433236885ca06f4b))

* build: optimize the development environment configuration guidance ([`a917e48`](https://github.com/irtnog/stuart/commit/a917e48166d9239faca608c1927ffe0c9830528a))

* build: combine continuous integration jobs into a single, well-documented workflow ([`dd2d912`](https://github.com/irtnog/stuart/commit/dd2d9126aeb30ef27c2f098b06647bbee496c9f9))

* build: update pre-commit hooks ([`5b85bc0`](https://github.com/irtnog/stuart/commit/5b85bc083b27323cf5ee2aef9e99ea62c016a37f))

* build: check whether commit messages follow Conventional Commits ([`0f3724b`](https://github.com/irtnog/stuart/commit/0f3724b10f3f85987f13c7f1c5efe6a5c8119808))

* build: switch to GNU Make ([`bd7297b`](https://github.com/irtnog/stuart/commit/bd7297b5ac9776426aae1f33a9623c453a92651f))

* build(packaging): canonicalize Python package names ([`f6a08f0`](https://github.com/irtnog/stuart/commit/f6a08f019e82b17a0a3780e9e78ac46e0ab83d87))

* build(packaging): remove unused/outdated dependency ([`f96a65e`](https://github.com/irtnog/stuart/commit/f96a65e4c27e336c671e37d9a10c9324908d04ec))

* build: mark phony make targets to avoid inadvertent conflicts with real files/directories ([`859c3ee`](https://github.com/irtnog/stuart/commit/859c3eeaf21e3f233011f2af83ff7be0225f88cc))

* build: add bashbrew and manifest-tool to the development environment ([`174557d`](https://github.com/irtnog/stuart/commit/174557d802a565c3bdd5ff8a6ccd891ff50bc6d4))

* build: install or activate the development environment automatically in Emacs

This requires enabling
[`pyvenv-mode`](https://github.com/jorgenschaefer/pyvenv). ([`90349f7`](https://github.com/irtnog/stuart/commit/90349f74508549a0b02037a1aaff12511070f692))

* build: replace aliases in target dependency lists with the actual artifacts in question

Otherwise, make will re-run targets unnecessarily. ([`7994a4c`](https://github.com/irtnog/stuart/commit/7994a4c5ae5ab3e9e3133eee75f3ba9383e0e05c))

### Documentation

* docs: advocate for good Python code styles with some static badges ([`c7e6052`](https://github.com/irtnog/stuart/commit/c7e60523e32cc9b4842509bc99073c0193dc100a))

* docs(packaging): update project description to match other documentation ([`1c1cff3`](https://github.com/irtnog/stuart/commit/1c1cff32c9ed949c080e3d10fb03350da4230893))

* docs: update the project&#39;s description ([`112f5d6`](https://github.com/irtnog/stuart/commit/112f5d629af6cc625734338771ef2bd9fe202fc4))

### Feature

* feat(systems): get a system from the database ([`cf014f9`](https://github.com/irtnog/stuart/commit/cf014f986621642e487e4e810a96621934f38558))

* feat(systems): outline the interface to system data ([`41b4abc`](https://github.com/irtnog/stuart/commit/41b4abc131dd482f6ce4a53d029754d5a401c681))

* feat: create a basic front end using Bootstrap 5 ([`e3b4d12`](https://github.com/irtnog/stuart/commit/e3b4d1295a641145a580bb15c1ef860d8760f594))

* feat: implement HTTP security response headers using Talisman ([`b4d4d01`](https://github.com/irtnog/stuart/commit/b4d4d015177c03bd69e4a74bd4d47d80b43237dd))

### Fix

* fix(app): load the specified test config even if the mapping is empty ([`e05e6d3`](https://github.com/irtnog/stuart/commit/e05e6d3b04e1285d02a7406fa9995566b7df79a3))

* fix: add missing favicon

I used https://favicon.io/ to generate this from my picture of the
central pulsar-white dwarf binary in [Double Dare (Dryaa Pruae DL-Y
e8379)](https://imgur.com/gallery/uM8uPFT), a system near the Neutron
Nebula. ([`387417d`](https://github.com/irtnog/stuart/commit/387417dda60a107523108d66759124e34b43c1b3))

### Refactor

* refactor(main): remove superfluous URL prefix ([`e3f9b7d`](https://github.com/irtnog/stuart/commit/e3f9b7d7ca062e11d6c58fac08eb638c354774c6))

* refactor(main): use the traditional name for the root web page ([`a4cb006`](https://github.com/irtnog/stuart/commit/a4cb006f29ab86aefc32b56e31c8e1e3593afc0a))

### Style

* style: adopt the Google Markdown style guide ([`0d0758f`](https://github.com/irtnog/stuart/commit/0d0758fcc069e20aab6cda4ff43f28c5cdb15ccd))

### Test

* test(app): rename test to better reflect its scope ([`11865d6`](https://github.com/irtnog/stuart/commit/11865d631c2813fe8bf2bbc0c77202f1640e1a1e))

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

### Unknown

* ci: grant python-semantic-release permission to update the GitHub repo ([`117ac2e`](https://github.com/irtnog/stuart/commit/117ac2e49d0ed9d349181ba093999da893d0ef95))

* ci: automate releases ([`4234625`](https://github.com/irtnog/stuart/commit/42346259f1a4c639a0b54e2ba47341ed2c7a214d))

* ci: run tests after linting ([`de62e92`](https://github.com/irtnog/stuart/commit/de62e926712192c84b8ae688ca24c034e9725876))

* ci: reuse the pre-commit hook ([`368e614`](https://github.com/irtnog/stuart/commit/368e61416b68a14aec0cd499d1f1fcfc602605d1))
