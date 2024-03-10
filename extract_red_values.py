from PIL import Image
import numpy as np
import sys

def is_color_in_range(pixel, target_color, tolerance):
    return all([abs(pixel[i] - target_color[i]) <= tolerance for i in range(3)])

def average_y_coordinate(image_path, target_color, tolerance=3):
    with Image.open(image_path) as img:
        img_data = np.array(img)
        height, width, _ = img_data.shape
        average_y_per_column = []

        for x in range(width):
            y_coords = []
            for y in range(height):
                if is_color_in_range(img_data[y, x], target_color, tolerance):
                    y_coords.append(y)

            if y_coords:
                average_y = sum(y_coords) / len(y_coords)
                average_y_per_column.append((x, average_y))
            else:
                pass
                #average_y_per_column.append((x, None))

        return average_y_per_column

# Usage
image_path = sys.argv[1]
target_color = [251, 49, 89]  # Target RGB color
tolerance = 3  # Tolerance for each RGB component

average_y = average_y_coordinate(image_path, target_color, tolerance)
for i, v  in enumerate(average_y):
    print(v[0],v[1])
#print(average_y)
