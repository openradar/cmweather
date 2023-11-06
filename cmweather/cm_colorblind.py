"""
Colorblind friendly radar colormaps

Available colormaps, reversed versions are also provided, these
colormaps are available within matplotlib:

    * HomeyerRainbow
    * balance
    * ChaseSpectral
    * SpectralExtended
    * CM_depol
    * CM_rhohv
    * plasmidis

CM_dopol and CM_rhohv are based on the work by:

Crameri, F., G.E. Shephard and P.J. Heron, 2020: The misuse of colour in science
communication. Nat Commun 11, 5444 https://doi.org/10.1038/s41467-020-19160-7

Michelson D., B. Hansen, D. Jacques, F. Lemay, and P Rodriguez, 2020: Monitoring
the impact of weather radar data quality control for quantitative application
at the continental scale. Meteorol. Appl. 2020;27:e1929. 12 pp.
https://doi.org/10.1002/met.1929

"""

import warnings

import matplotlib as mpl
import matplotlib.colors as colors

from ._cm_colorblind import datad
from .cm import _reverse_cmap_spec


def _generate_cmap(name, lutsize):
    """Generates the requested cmap from it's name *name*. The lut size is
    *lutsize*."""

    spec = datad[name]
    # Generate the colormap object.
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', FutureWarning)
        if isinstance(spec, dict) and 'red' in spec.keys():
            return colors.LinearSegmentedColormap(name, spec, lutsize)
        else:
            return colors.LinearSegmentedColormap.from_list(name, spec, lutsize)


cmap_d = dict()

# reverse all the colormaps.
# reversed colormaps have '_r' appended to the name.

LUTSIZE = mpl.rcParams['image.lut']

# need this list because datad is changed in loop
_cmapnames = list(datad.keys())

# Generate the reversed specifications ...

for cmapname in _cmapnames:
    spec = datad[cmapname]
    spec_reversed = _reverse_cmap_spec(spec)
    datad[cmapname + '_r'] = spec_reversed

# Precache the cmaps with ``lutsize = LUTSIZE`` ...

# Use datad.keys() to also add the reversed ones added in the section above:
for cmapname in datad.keys():
    cmap_d[cmapname] = _generate_cmap(cmapname, LUTSIZE)

locals().update(cmap_d)

# register the colormaps so that can be accessed with the names pyart_XXX
for name, cmap in cmap_d.items():
    # Matplotlib 3.6.0 colormap registering changed.
    try:
        mpl.colormaps.register(name=name, cmap=cmap, force=True)
    except AttributeError:
        mpl.cm.register_cmap(name=name, cmap=cmap)
