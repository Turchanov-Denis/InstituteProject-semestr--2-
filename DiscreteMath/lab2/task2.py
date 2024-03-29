def find_term(n):
    C1 = 5 / 7
    C2 = 2 / 7
    return C1 * 2**n + C2 * (-5)**n


result1 = find_term(100)
print("a(100) =", result1)


def calculate_a(n):
    a = [1, 1]
    for n in range(2, n):
        a.append(-3 * a[n-1] + 10 * a[n-2])
    return a

result2 = calculate_a(100)
print("a_100 =", result2)
