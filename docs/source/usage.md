---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  name: python3
---

# Usage

## Installing cmweather

cmweather can be installed in three ways:

```{eval-rst}

.. tab-set::

    .. tab-item:: conda

        Using the `conda <https://conda.io/>`__ package manager that comes with the
        Anaconda/Miniconda/Mamba distribution:

        .. code:: bash

            $ mamba install cmweather --channel conda-forge

    .. tab-item:: pip

        Using the `pip <https://pypi.org/project/pip/>`__ package manager:

        .. code:: bash

            $ python -m pip install cmweather

    .. tab-item:: Development version

        To install a development version from source:

        .. code:: bash

            $ git clone https://github.com/openradar/cmweather
            $ cd cmweather
            $ python -m pip install -e .
```

## Use cmweather In Your Scripts/Notebooks

You can use **cmweather** colormaps as you would use **matplotlib** colormaps in your workflow.

The first step is to import cmweather.

```{code-cell} ipython3
import cmweather

```

### RECOMMENDED: Try out a Color Vision Deficiency (CVD) Friendly Colormaps

It is recommended you try one of the CVD-friendly colormaps included in cmweather, such as ChaseSpectral

```{code-cell} ipython3
import cmweather
import numpy as np
import matplotlib.pyplot as plt

# Create some synthetic data
x = np.arange(1, 100)
y = np.arange(1, 100, .5)
x_2d, y_2d = np.meshgrid(x, y)
temps = (x_2d + y_2d)/2

# Plot our data and add a colorbar
color = plt.pcolormesh(temps, cmap='ChaseSpectral')
plt.colorbar(color);
```

### Using "Traditional" Colormaps

We can also use other colormaps such as the National Weather Service (NWS) Reflectivity (`NWSRef`) colormap with our plot

```{code-cell} ipython3
import cmweather
import numpy as np
import matplotlib.pyplot as plt

# Create some synthetic data
x = np.arange(1, 100)
y = np.arange(1, 100, .5)
x_2d, y_2d = np.meshgrid(x, y)
temps = (x_2d + y_2d)/2

# Plot our data and add a colorbar
color = plt.pcolormesh(temps, cmap='NWSRef')
plt.colorbar(color);
```

A full list of colormaps can be found in the [Reference](api.md) section of the docs
