# Simple program to calculate the distance between two points in 2D space using the distance formula.
# by Claudio Vincenzo Catalano Leiva - 2026-02-26 for the Data Science Seminar 3 - The Scientific Paper of the Future

import math

"""
Calculate the distance between two points in 2D space.

Parameters:
point1 (tuple): The first point as a tuple (x1, y1).
point2 (tuple): The second point as a tuple (x2, y2).

Returns:
float: The distance between the two points.
"""
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Main block to execute the program
if __name__ == "__main__":
    try:
        x1, y1, x2, y2 = map(float, [input("Input x1: "), input("and y1: "), input("Input x2: "), input("and y2: ")])
        point_a, point_b = (x1, y1), (x2, y2)
        distance = calculate_distance(point_a, point_b)
        print(f"Distance between {point_a} and {point_b}: {distance:.2f} units.")
    except ValueError:
        print("Please enter numeric coordinates.")