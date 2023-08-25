# cmweather

```{image} https://github.com/openradar/cmweather/actions/workflows/ci.yaml/badge.svg
:alt: Continuous Integration Status
:target: https://github.com/openradar/cmweather/actions/workflows/ci.yaml
```

```{image} https://github.com/openradar/cmweather/actions/workflows/linting.yaml/badge.svg
:alt: Code Style Status
:target: https://github.com/openradar/cmweather/actions/workflows/linting.yaml
```

```{image} https://img.shields.io/codecov/c/github/openradar/cmweather.svg?style=for-the-badge
:target: https://codecov.io/gh/openradar/cmweather
```

% If you want the following badges to be visible, please remove this line, and unindent the lines below
% .. image:: https://img.shields.io/readthedocs/cmweather/latest.svg?style=for-the-badge
% :target: https://cmweather.readthedocs.io/en/latest/?badge=latest
% :alt: Documentation Status
%
% .. image:: https://img.shields.io/pypi/v/cmweather.svg?style=for-the-badge
% :target: https://pypi.org/project/cmweather
% :alt: Python Package Index
%
% .. image:: https://img.shields.io/conda/vn/conda-forge/cmweather.svg?style=for-the-badge
% :target: https://anaconda.org/conda-forge/cmweather
% :alt: Conda Version

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

These code style pre-commit hooks (black, isort, flake8, ...) will run every time you are about to commit code.

% If you want the following badges to be visible, please remove this line, and unindent the lines below
% Re-create notebooks with Pangeo Binder
% --------------------------------------
%
% Try notebooks hosted in this repo on Pangeo Binder. Note that the session is ephemeral.
% Your home directory will not persist, so remember to download your notebooks if you
% made changes that you need to use at a later time!
%
% .. image:: https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=GCE+us-central1&color=blue&style=for-the-badge
% :target: https://binder.pangeo.io/v2/gh/openradar/cmweather/master?urlpath=lab
% :alt: Binder
