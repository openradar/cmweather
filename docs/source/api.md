---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  name: python3
---

# Reference

## Color Vision Deficiency Friendly Colormaps (`cmweather.cm_colorblind`)

```{eval-rst}
.. automodule:: cmweather.cm_colorblind
    :members:
    :undoc-members:
    :show-inheritance:
```

```{code-cell} ipython3
:tags: [remove-input]

from IPython.display import HTML
from cmweather.cm_colorblind import cmap_d
from cmweather.cm import _get_cmap_gallery_html

html_str = _get_cmap_gallery_html(cmap_d, sort_d=False)
display(HTML(html_str))
```

## More Weather Colormaps (`cmweather.cm`)

```{eval-rst}
.. automodule:: cmweather.cm
    :members:
    :undoc-members:
    :show-inheritance:
```

```{code-cell} ipython3
:tags: [remove-input]

from IPython.display import HTML
from cmweather.cm import cmap_d, _get_cmap_gallery_html

html_str = _get_cmap_gallery_html(cmap_d, sort_d=True)
display(HTML(html_str))
```
