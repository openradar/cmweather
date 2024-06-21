"""
Radar related colormaps.

Available colormaps, reversed versions (_r) are also provided, these
colormaps are available within matplotlib:

    * BlueBrown10
    * BlueBrown11
    * BrBu10
    * BrBu12
    * Bu10
    * Bu7
    * BuDOr12
    * BuDOr18
    * BuDRd12
    * BuDRd18
    * BuGr14
    * BuGy8
    * BuOr10
    * BuOr12
    * BuOr8
    * BuOrR14
    * Carbone11
    * Carbone17
    * Carbone42
    * Cat12
    * EWilson17
    * GrMg16
    * Gray5
    * Gray9
    * NWSRef
    * NWSVel
    * NWS_SPW
    * NWS_CC
    * PD17
    * RRate11
    * RdYlBu11b
    * RefDiff
    * SCook18
    * StepSeq25
    * SymGray12
    * Theodore16
    * Wild25
    * LangRainbow12

"""

# This file was adapted from the cm.py file of the matplotlib project,
# http://matplotlib.org/.
# Copyright (c) 2012-2013 Matplotlib Development Team; All Rights Reserved

import warnings

import matplotlib as mpl
import matplotlib.colors as colors

from ._cm import datad

cmap_d = dict()

# reverse all the colormaps.
# reversed colormaps have '_r' appended to the name.


def _reverser(f):
    """perform reversal."""

    def freversed(x):
        """f specific reverser."""
        return f(1 - x)

    return freversed


def revcmap(data):
    """Can only handle specification *data* in dictionary format."""
    data_r = {}
    for key, val in data.items():
        if callable(val):
            valnew = _reverser(val)
            # This doesn't work: lambda x: val(1-x)
            # The same "val" (the first one) is used
            # each time, so the colors are identical
            # and the result is shades of gray.
        else:
            # Flip x and exchange the y values facing x = 0 and x = 1.
            valnew = [(1.0 - x, y1, y0) for x, y0, y1 in reversed(val)]
        data_r[key] = valnew
    return data_r


def _reverse_cmap_spec(spec):
    """Reverses cmap specification *spec*, can handle both dict and tuple
    type specs."""
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', FutureWarning)
        if isinstance(spec, dict) and 'red' in spec.keys():
            return revcmap(spec)
        else:
            revspec = list(reversed(spec))
            if len(revspec[0]) == 2:  # e.g., (1, (1.0, 0.0, 1.0))
                revspec = [(1.0 - a, b) for a, b in revspec]
            return revspec


def _generate_cmap(name, lutsize):
    """Generates the requested cmap from it's name *name*.  The lut size is
    *lutsize*."""

    spec = datad[name]

    # Generate the colormap object.
    if isinstance(spec, dict) and 'red' in spec.keys():
        return colors.LinearSegmentedColormap(name, spec, lutsize)
    else:
        return colors.LinearSegmentedColormap.from_list(name, spec, lutsize)


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


def _get_cmap_gallery_html(cmaps, sort_d=False):
    """
    return a html str representation of a colormap dictionary

    use with either cmap_d from either .cm or .cm_colorblind,
    reversed colormaps are excluded. The html repr of
    individual colormaps is based on what the base
    matplotlib.colors.Colormap._repr_html_() returns but
    without the "over", "under" and "bad" labels.

    Parameters
    ----------
    cmaps: dict
        a dictionary of colormaps
    sort_d: bool
        if True (default False), will sort the cmaps by name

    Returns
    -------
    str
        the concatenated html str for the input colormap dict

    """
    import base64

    def _get_cmap_div(cmap):
        png_bytes = cmap._repr_png_()
        png_base64 = base64.b64encode(png_bytes).decode('ascii')

        return (
            '<div style="vertical-align: middle;">'
            f'<strong>{cmap.name}</strong> '
            '</div>'
            '<div class="cmap"><img '
            f'alt="{cmap.name} colormap" '
            f'title="{cmap.name}" '
            'style="border: 1px solid #555;" '
            f'src="data:image/png;base64,{png_base64}"></div>'
        )

    cm_names = [cnm for cnm in cmaps.keys() if not cnm.endswith('_r')]
    if sort_d:
        cm_names.sort()

    html_str = ''
    for cm_name in cm_names:
        html_str += _get_cmap_div(cmaps[cm_name])

    return html_str
