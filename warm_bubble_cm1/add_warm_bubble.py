# ------------------------------------------------
# Name: add_warm_bubble.py
# Author: Robby M. Frost
# University of Oklahoma
# Created: 17 September 2024
# Purpose: Add a warm bubble to a CM1 restart file
# ------------------------------------------------

import xarray as xr
import numpy as np

# ---------------------------
# read in restart file

df = np.fromfile('/Users/robbyfrost/Documents/MS_Project/warm_bubble_cm1/cm1out_rst_000013_x.dat', dtype=np.float32)