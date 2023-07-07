""" Unit Tests for cmweather's cm.py module. """


import matplotlib

from cmweather import cm


def test_colormaps_exist():
    assert isinstance(cm.NWSRef, matplotlib.colors.Colormap)
    assert isinstance(cm.NWSRef_r, matplotlib.colors.Colormap)


def test_colormaps_registered():
    cmap = matplotlib.colormaps.get_cmap('NWSRef')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('NWSRef_r')
    assert isinstance(cmap, matplotlib.colors.Colormap)


def test_tuple_spec():
    # None of the cmweather colormaps use the tuple spec, so for coverage in the
    # unit tests define a colormap using a tuple

    # data borrowed from matplotlib's lib/matplotlib/_cm.py
    _seismic_data = (
        (0.0, 0.0, 0.3),
        (0.0, 0.0, 1.0),
        (1.0, 1.0, 1.0),
        (1.0, 0.0, 0.0),
        (0.5, 0.0, 0.0),
    )
    cm._reverse_cmap_spec(_seismic_data)

    spec = ((0, 1), (0, 1))
    cm._reverse_cmap_spec(spec)

    cm.datad['foo'] = _seismic_data
    cm._generate_cmap('foo', 1)
    assert isinstance(cm.NWSRef_r, matplotlib.colors.Colormap)


def test_revcmap_callable():
    # reversing a callable is not exercised in cmweather
    data_r = cm.revcmap({'foo': lambda x: x})
    assert data_r['foo'](0) == 1
