# Решить задачу о суммах подмножеств, используя жадный алгоритм.
def subset_sum_greedy(set, sum):
    set.sort(reverse=True)
    subset = []
    remaining_sum = sum
    for element in set:
        if remaining_sum - element >= 0:
            subset.append(element)
            remaining_sum -= element
    return subset, remaining_sum

# Example usage
set = [1, 2, 5, 3, 34, 12, 2]
sum = 35
subset, remaining_sum = subset_sum_greedy(set, sum)
print("Found subset:", subset)
print("Remaining sum:", remaining_sum)