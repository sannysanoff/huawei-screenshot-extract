import cv2
import numpy as np
import sys

def group_consecutive(arr):
    # Find the difference between consecutive values
    diffs = np.diff(arr)
    # Identify the start of a new group (difference != 1)
    group_starts = np.where(diffs != 1)[0] + 1
    # Include the first value of the array as the start of the first group
    group_starts = np.insert(group_starts, 0, 0)
    # Select the first value of each group
    return arr[group_starts]

def find_y_ticks(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to RGB (OpenCV uses BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("# image w,h=",len(image_rgb[0]),len(image_rgb))
    print("# ",image[5][5])

    # Find the y-axis line by looking for the first vertical line with a cumulative excess of red
    red_sums = np.mean(image_rgb[:, :, 0], axis=0)  # sum of red channel values in each column
    green_sums = np.mean(image_rgb[:, :, 1], axis=0)
    blue_sums = np.mean(image_rgb[:, :, 2], axis=0)
    y_axis_x_coord = None

    # Loop through each column to find the y-axis line
    for i, red_sum in enumerate(red_sums):
        if red_sum > green_sums[i] and red_sum > blue_sums[i]:
            y_axis_x_coord = i
            print("# found x of y axis:",i)
            break

    # Verify if we found a y-axis line
    if y_axis_x_coord is None:
        raise ValueError("Couldn't find the y-axis line.")

    # Subtract a few pixels to the left to avoid the actual y-axis line
    y_axis_x_coord -= 2

    # Find y coordinates of pixels with 229,229,229 RGB values
    gray_line_y_coords = []
    for y in range(image_rgb.shape[0]):
        if np.array_equal(image_rgb[y, y_axis_x_coord], np.array([229, 229, 229])):
            gray_line_y_coords.append(y)

    gray_line_y_coords = group_consecutive(np.array(gray_line_y_coords))

    # Check that the y coordinates form a mathematical progression (constant interval)
    intervals = np.diff(gray_line_y_coords)
    mean_interval = np.mean(intervals)
    print("# mean ",mean_interval)

    # Filter out any outliers that do not conform to the progression (use mean_interval +/- 10% as threshold)
    accepted_gray_line_y_coords = [gray_line_y_coords[0]]  # Always include the first coordinate
    for i in range(1, len(gray_line_y_coords)):
        if abs(intervals[i-1] - mean_interval) <= 0.1 * mean_interval:
            accepted_gray_line_y_coords.append(gray_line_y_coords[i])

    return accepted_gray_line_y_coords

# Replace 'your_image_path.jpg' with your actual image path
y_ticks = find_y_ticks(sys.argv[1])
for y in y_ticks:
    print(y)

