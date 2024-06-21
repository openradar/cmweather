import pytest

from cmweather import cm, cm_colorblind


@pytest.mark.parametrize('cmap_d,sort_d', [(cm.cmap_d, True), (cm_colorblind.cmap_d, False)])
def test_get_cmap_gallery_html(cmap_d, sort_d):
    html_str = cm._get_cmap_gallery_html(cmap_d, sort_d=sort_d)

    assert isinstance(html_str, str)
    assert len(html_str) > 0
    assert html_str.startswith('<div')
    assert html_str.endswith('</div>')
