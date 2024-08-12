# cmweather

[![CI Status](https://github.com/openradar/cmweather/actions/workflows/ci.yaml/badge.svg)](https://github.com/openradar/cmweather/actions/workflows/ci.yaml) [![code-style](https://github.com/openradar/cmweather/actions/workflows/linting.yaml/badge.svg)](https://github.com/openradar/cmweather/actions/workflows/linting.yaml) [![CodeCov](https://img.shields.io/codecov/c/github/openradar/cmweather.svg?style=for-the-badge)](https://codecov.io/gh/openradar/cmweather)[![Conda Package](https://anaconda.org/conda-forge/cmweather/badges/version.svg)](https://anaconda.org/conda-forge/cmweather)

## Motivation

The motivation for this package is to contain weather maps relevant to the weather and climate community. There are **many** colormaps that are unique to the weather/climate community that are not included in core libraries such as [matplotlib](https://matplotlib.org/). This is also meant to be a community collaboration, across multiple domain-specific packages (ex. MetPy, GeoCAT, Py-ART). It is lightweight, easy to install, and we encourage contributions from across the community!

While not all of the colormaps are color vision deficiency (CVD) friendly, we do include CVD friendly colormaps, and encourage users to use these when possible.

## Citing

When using the CVD friendly colormaps, please consider citing:

Sherman, Z., and Coauthors, 2024: Effective Visualization of Radar Data for Users Impacted by Color Vision Deficiency. Bull. Amer. Meteor. Soc., 105, E1479–E1489, https://doi.org/10.1175/BAMS-D-23-0056.1.

And when using the CVD friendly cmocean balance colormap, please cite:

Thyng, K. M., C. A. Greene, R. D. Hetland, H. M. Zimmerle, and S. F. DiMarco, 2016: True colors of oceanography: Guidelines for effective and accurate colormap selection. Oceanography, 29, 9–13, https://doi.org/10.5670/oceanog.2016.66.

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
