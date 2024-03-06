def rotate(A, B, C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])


def jarvismarch(A):
    n = len(A)
    P = list(range(n))
    # start point
    for i in range(n):
        if (A[P[i]][0] <= A[P[0]][0]) & (A[P[i]][1] < A[P[0]][1]):
            P[i], P[0] = P[0], P[i]
    H = [P[0]]
    del P[0]
    P.append(H[0])
    while True:
        right = 0
        for i in range(1, len(P)):
            if rotate(A[H[-1]], A[P[right]], A[P[i]]) < 0:
                right = i
        if P[right] == H[0]:
            break
        else:
            H.append(P[right])
            del P[right]
    return H


points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

for i in jarvismarch(points):
    print(points[i])