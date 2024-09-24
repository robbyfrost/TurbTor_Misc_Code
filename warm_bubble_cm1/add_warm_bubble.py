# ------------------------------------------------
# Name: add_warm_bubble.py
# Author: Robby M. Frost
# University of Oklahoma
# Created: 17 September 2024
# Purpose: Add a warm bubble to a CM1 restart file
# ------------------------------------------------

import struct
import numpy as np

# ---------------------------
# read in restart file

# Define the dimensions of the model domain
nx, ny, nz = 1700, 1700, 121  # Replace with actual dimensions of your model

# Calculate the number of grid points
num_points = nx * ny * nz

# Define the path to the restart file
file_path = '/Users/robbyfrost/Documents/MS_Project/TurbTor_Misc_Code/warm_bubble_cm1/cm1out_rst_000013_s.dat'

# Define the format string for struct.unpack
# Assuming 4 variables (e.g., u, v, w, th) and each is a float32
data_format = f'{4 * num_points}f'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Read the data and unpack using struct
    file_content = file.read()
    data = struct.unpack(data_format, file_content)

# Convert the unpacked data to a NumPy array for easy manipulation
data_array = np.array(data, dtype='float32')

# Extract the variables from the flat data array
u = data_array[0:num_points].reshape((nx, ny, nz))
v = data_array[num_points:2*num_points].reshape((nx, ny, nz))
w = data_array[2*num_points:3*num_points].reshape((nx, ny, nz))
th = data_array[3*num_points:4*num_points].reshape((nx, ny, nz))
