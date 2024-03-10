import numpy as np
from scipy import stats
import re
import sys

# Data from file1.txt
exacty_data = [
    (157, 162),
    (138, 280),
    (119, 399),
    (100, 517)
]

exactx_data = [
    ("00:00:00", 82.0),
    ("00:01:40", 324.0),
    ("00:03:20", 565.5),
    ("00:05:00", 808.0),
    ("00:06:40", 1050.0),
    ("00:08:20", 1292.0),
    ("00:10:00", 1534.0),
    ("00:11:40", 1774.0),
    ("00:13:20", 2016.0)
]

def read_file1(filename):
    exacty_data = []
    exactx_data = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if parts[0] == 'exacty':
                exacty_data.append((int(parts[2]), float(parts[1])))
            elif parts[0] == 'exactx':
                exactx_data.append((parts[1], float(parts[2])))

    return exacty_data, exactx_data

def read_file2(filename):
    file2_data = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            file2_data.append((int(parts[0]), float(parts[1])))

    return file2_data

# Convert time HH:MM:SS to seconds
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

exacty_data, exactx_data = read_file1(sys.argv[1])
file2_data = read_file2(sys.argv[2])

# Prepare data for linear regression
y_image, y_physical = zip(*exacty_data)
x_image, x_time = zip(*[(x, time_to_seconds(t)) for t, x in exactx_data])

# Calculate linear regression for y
slope_y, intercept_y, _, _, _ = stats.linregress(y_image, y_physical)

# Calculate linear regression for x
slope_x, intercept_x, _, _, _ = stats.linregress(x_image, x_time)

transformed_data = [(slope_x * x + intercept_x, slope_y * y + intercept_y) for x, y in file2_data]
for i, v in enumerate(transformed_data):
   print(v[0], v[1])

