# cmweather

[![CI Status](https://github.com/openradar/cmweather/actions/workflows/ci.yaml/badge.svg)](https://github.com/openradar/cmweather/actions/workflows/ci.yaml) [![code-style](https://github.com/openradar/cmweather/actions/workflows/linting.yaml/badge.svg)](https://github.com/openradar/cmweather/actions/workflows/linting.yaml) [![CodeCov](https://img.shields.io/codecov/c/github/openradar/cmweather.svg?style=for-the-badge)](https://codecov.io/gh/openradar/cmweather)[![Conda Package](https://anaconda.org/conda-forge/cmweather/badges/version.svg)](https://anaconda.org/conda-forge/cmweather)

## Motivation

The motivation for this package is to contain weather maps relevant to the weather and climate community. There are **many** colormaps that are unique to the weather/climate community that are not included in core libraries such as [matplotlib](https://matplotlib.org/). This is also meant to be a community collaboration, across multiple domain-specific packages (ex. MetPy, GeoCAT, Py-ART). It is lightweight, easy to install, and we encourage contributions from across the community!

While not all of the colormaps are color vision deficiency (CVD) friendly, we do include CVD friendly colormaps, and encourage users to use these when possible.

## Installation

cmweather can be found on both PyPI and conda-forge, installable using

```bash
mamba install cmweather
```

or

```bash
pip install cmweather
```

### Development Installation

For a development install, do the following in the repository directory:

```bash
conda env update -f ci/environment.yml
conda activate cmweather-dev
python -m pip install -e .
```

Also, please install `pre-commit` hooks from the root directory of the created project by running:

```
pre-commit install
```
