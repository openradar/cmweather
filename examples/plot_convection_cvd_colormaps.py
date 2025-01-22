"""
=========================================================
Plotting a Convective System using CVD Friendly Colormaps
=========================================================

This is an example of using both HomeyerRainbow and ChaseSpectral CVD friendly
colormaps for a convective system in Oklahoma.

"""
print(__doc__)

# Author: Zach Sherman
# License: BSD 3 clause

import matplotlib.pyplot as plt
import pyart
from open_radar_data import DATASETS

import cmweather  # noqa

######################################
# **Download and read in the data**
#
# First we will read in the example data from the repository open_radar_data
# by using a built in fetch function to download the data.

file = DATASETS.fetch('110635.nc')

# Read the data using pyart
radar = pyart.io.read(file)

# Apply a filter to remove ring artifact
gatefilter = pyart.filters.GateFilter(radar)
gatefilter.exclude_last_gates('reflectivity', n_gates=7)

######################################
# **Color Vision Deficiency (CVD) Friendly Colormap HomeyerRainbow**
#
# Let's visualize the HomeyerRainbow CVD friendly colormap for the reflectivity
# moment in our data.

# create the plot using RadarDisplay
display = pyart.graph.RadarDisplay(radar)
fig = plt.figure()
display.plot(
    'reflectivity',
    0,
    vmin=-16.0,
    vmax=64,
    title='PPI',
    cmap='HomeyerRainbow',
    gatefilter=gatefilter,
)
display.set_limits(ylim=[-150, 150], xlim=[-150, 150])
plt.show()

#######################################
# **Color Vision Deficiency (CVD) Friendly Colormap ChaseSpectral**
#
# Similar to the previous example, let's visualize the ChaseSpectral CVD
# friendly colormap

# create the plot using RadarDisplay
display = pyart.graph.RadarDisplay(radar)
fig = plt.figure()
display.plot(
    'reflectivity',
    0,
    vmin=-16.0,
    vmax=64,
    title='PPI',
    cmap='ChaseSpectral',
    gatefilter=gatefilter,
)
display.set_limits(ylim=[-150, 150], xlim=[-150, 150])
plt.show()
