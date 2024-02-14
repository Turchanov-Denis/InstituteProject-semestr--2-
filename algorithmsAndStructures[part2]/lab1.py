def orientation(p, q, r):
    """
    Function to determine the orientation of three points (turn)
    :param p: First point (x, y)
    :param q: Second point (x, y)
    :param r: Third point (x, y)
    :return: 0 if points are collinear, 1 if clockwise orientation, -1 otherwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def jarvis_march(points):
    """
    Function to construct convex hull using Jarvis March algorithm
    :param points: Set of points (x, y)
    :return: List of vertices of the convex hull
    """
    n = len(points)
    if n < 3:
        return []

    # Find the point with the lowest y-coordinate (or lowest x if y is equal)
    start_point = min(points)

    hull = []
    current_point = start_point
    next_point = None

    while True:
        hull.append(current_point)
        next_point = (current_point[0] + 1, current_point[1])  # Assume next point will be the one to the right of the current point
        for candidate_point in points:
            if candidate_point == current_point:
                continue
            if next_point == current_point or orientation(current_point, next_point, candidate_point) == -1:  
                next_point = candidate_point

        # If we've reached the start point, finish the algorithm
        if next_point == start_point:
            break

        current_point = next_point  # Move to the next point

    return hull

if __name__=="__main__":
    # Example usage:
    points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    convex_hull = jarvis_march(points)
    print("Convex hull:", convex_hull)
