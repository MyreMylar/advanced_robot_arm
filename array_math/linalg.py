import math


def norm(vector):
    total_sq = 0
    for param in vector:
        total_sq += param**2
    return math.sqrt(total_sq)
