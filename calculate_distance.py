# Simple program to calculate the distance between two points in 2D space using the distance formula.
# by Claudio Vincenzo Catalano Leiva - 2026-02-26 for the Data Science Seminar 3 - The Scientific Paper of the Future

import math

def calculate_distance(point1, point2):
    """
    Calculate the distance between two points in 2D space.

    Parameters:
    point1 (tuple): The first point as a tuple (x1, y1).
    point2 (tuple): The second point as a tuple (x2, y2).

    Returns:
    float: The distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Example usage
if __name__ == "__main__":
    print("Input the coordinate x1: ")
    x1 = input()

    print("Input the coordinate y1: ")
    y1 = input()

    print("Input the coordinate x2: ")
    x2 = input()

    print("Input the coordinate y2: ")
    y2 = input()

    point_a = (int(x1), int(y1))
    point_b = (int(x2), int(y2))
    distance = calculate_distance(point_a, point_b)
    print(f"The distance between {point_a} and {point_b} is: {distance:.2f} units.")