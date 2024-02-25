def orientation(p, q, r):
    """
    Функция для определения ориентации троек точек (p, q, r).
    Возвращает:
     - 0, если точки p, q и r коллинеарны (лежат на одной прямой).
     - 1, если точка r находится по часовой стрелке от отрезка pq (поворот направо).
     - 2, если точка r находится против часовой стрелки от отрезка pq (поворот налево).
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    """
    Функция для нахождения выпуклой оболочки с использованием алгоритма Джарвиса.
    """
    n = len(points)
    if n < 3:
        return "Недостаточно точек"

    # Находим самую левую нижнюю точку
    leftmost = min(points)

    def next_hull_point(p, hull):
        q = hull[0] if len(hull) == 1 else hull[-2]  # Предполагаем, что последняя точка на оболочке - это конечная точка.
        for r in points:
            if r == p:
                continue
            turn = orientation(p, q, r)
            if turn == 2 or (turn == 0 and r not in hull):
                q = r
        return q

    hull = []
    p = leftmost
    while True:
        hull.append(p)
        q = next_hull_point(p, hull)
        if q == leftmost:
            break
        p = q

    return hull

# Тестовый набор точек
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

# Получаем выпуклую оболочку
convex_hull_points = convex_hull(points)

# Проверяем результат
if len(convex_hull_points) < 3:
    print("Не существует выпуклой оболочки для данного множества точек")
else:
    print(convex_hull_points)
