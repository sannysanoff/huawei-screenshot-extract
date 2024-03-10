import sys
def read_inexact_coordinates(file_path):
    """Read inexact coordinates from the file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    inexact_coordinates = [(line.split()[1], int(line.split()[2])) for line in lines[1:]]  # Skip header
    return inexact_coordinates

def read_exact_coordinates(file_path):
    """Read exact coordinates from the file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    exact_coordinates = [int(line.strip()) for line in lines]
    return exact_coordinates

def find_closest(exact_coords, inexact_y):
    """Find the closest exact y-coordinate."""
    return min(exact_coords, key=lambda x: abs(x - inexact_y))

def assign_exact_coordinates(inexact_file, exact_file):
    inexact_coordinates = read_inexact_coordinates(inexact_file)
    exact_coordinates = read_exact_coordinates(exact_file)

    for label, inexact_y in inexact_coordinates:
        closest_exact_y = find_closest(exact_coordinates, inexact_y)
        print(f"exacty {label} {closest_exact_y}")

assign_exact_coordinates("/dev/stdin",sys.argv[1])
