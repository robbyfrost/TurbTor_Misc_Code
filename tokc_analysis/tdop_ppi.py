# ------------------------------------------------
# Name: tdop_ppi.py
# Author: Robby M. Frost
# University of Oklahoma
# Created: 23 September 23024
# Purpose: Plotting terminal doppler PPIs of radial
# velocity and inferred vertical vorticity
# ------------------------------------------------

import pyart
# import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# ---------------------------------
# read in radar file

# radar file location
dfile = '/Users/robbyfrost/Documents/MS_Project/data_tmp/tokc/TOKC20240714_215057_V08'

radar = pyart.io.read(dfile)

# extract radar position
radar_lat = radar.latitude['data'][0]
radar_lon = radar.longitude['data'][0]

# mask out last 10 gates of each ray, this removes the "ring" around the radar.
radar.fields["reflectivity"]["data"][:, -10:] = np.ma.masked

# exclude masked gates from the gridding
gatefilter = pyart.filters.GateFilter(radar)
gatefilter.exclude_transition()
gatefilter.exclude_masked("reflectivity")

# ---------------------------------
# plot PPI

# Create the display
fig = plt.figure(figsize=(10, 8))
projection = ccrs.PlateCarree()

# Create an axis with a map
ax = plt.axes(projection=projection)

# Add coastlines and other map features
ax.coastlines('50m')
ax.add_feature(cfeature.BORDERS, linewidth=1)
ax.add_feature(cfeature.STATES, linewidth=0.5)

# Define the radar's location (longitude and latitude)
lon, lat = radar.longitude['data'][0], radar.latitude['data'][0]

# Plot the PPI
display = pyart.graph.RadarMapDisplay(radar)
display.plot_ppi_map(
    'reflectivity',  # Field to plot, can change based on your radar variable
    sweep=0,  # Sweep level to display
    ax=ax,
    projection=ccrs.PlateCarree(),  # Using PlateCarree projection for the map
    min_lon=lon - 1, max_lon=lon + 1,  # Adjust the map extent
    min_lat=lat - 1, max_lat=lat + 1,
    resolution='50m',  # Cartopy map resolution
    lat_lines=np.arange(int(lat) - 1, int(lat) + 2, 0.5),
    lon_lines=np.arange(int(lon) - 1, int(lon) + 2, 0.5)
)

# Add a colorbar
plt.colorbar(display.plots[0], ax=ax, orientation='horizontal')

# Display the plot
plt.show()