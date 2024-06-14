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

cm_names = [cnm for cnm in cmap_d.keys() if not cnm.endswith('_r')]

for cm_name in cm_names:
    display(HTML(cmap_d[cm_name]._repr_html_()))
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
from cmweather.cm import cmap_d

cm_names = [cnm for cnm in cmap_d.keys() if not cnm.endswith('_r')]
cm_names.sort()

for cm_name in cm_names:
    display(HTML(cmap_d[cm_name]._repr_html_()))
```
