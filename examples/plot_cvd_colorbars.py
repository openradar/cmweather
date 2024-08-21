"""
===================================
Choose a CVD Colormap for your Plot
===================================

This is an example of some of the CVD friendly colormaps in cmweather,
and how to add them to your own plots.

"""
print(__doc__)

# Author: Max Grover and Zach Sherman
# License: BSD 3 clause

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import cmweather  # noqa

matplotlib.rcParams.update({'font.family': 'Arial'})

######################################
# **Plot the available colormaps**
#
# Let's see which CVD colormaps are available directly from cmweather!
# We use a helper function from matplotlib to plot this.

# Setup some helper functions and ranges to visualize our colormaps, from matplotlib
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.4, right=0.99)

    axs[0].set_title(cmap_category, fontsize=14)

    for ax, cmap_name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=f"{cmap_name}")
        if cmap_name == 'plasmidis':
            ax.text(
                -0.01,
                0.5,
                f"{'plasmidis'}",
                va='center',
                ha='right',
                fontsize=10,
                transform=ax.transAxes,
            )
        else:
            ax.text(
                -0.01,
                0.5,
                f"{cmap_name}",
                va='center',
                ha='right',
                fontsize=10,
                transform=ax.transAxes,
            )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()


######################################
# **Color Vision Deficiency (CVD) Friendly Colormaps**
#
# We recommend starting with these CVD friendly colormaps.
# These colormaps are the most inclusive, and should be used where
# possible.

#######################################
# **Reflectivity Colormaps
#
# These CVD colormaps were created for equivalent reflectivity factor.

(r'$H_{2}$')
plot_color_gradients(
    r'CVD-Friendly $Z_{e}$ Colormaps',
    ['LangRainbow12', 'HomeyerRainbow', 'ChaseSpectral', 'SpectralExtended'],
)

########################################
# **Velocity Colormaps
#
# These CVD colormaps were created for mean Doppler velocity.

plot_color_gradients('CVD-Friendly Velocity Colormaps', ['balance', 'twilight_shifted'])

########################################
# **Polarization Colormaps
# These CVD colormaps were created for polarization moments such as
# differential reflectivity and depolarization ratio.

plot_color_gradients('CVD-Friendly Polarization Colormaps', ['CM_depol', 'plasmidis'])
