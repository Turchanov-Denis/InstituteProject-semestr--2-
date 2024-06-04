def subset_sum_backtracking(S, T):
    # Сортируем множество S в порядке убывания
    S_sorted = sorted(S, reverse=True)
    
    def backtrack(start, current_sum, subset):
        # Если текущая сумма равна T, мы нашли нужное подмножество
        if current_sum == T:
            return subset
        
        # Если текущая сумма превышает T, возвращаем None
        if current_sum > T:
            return None
        
        for i in range(start, len(S_sorted)):
            num = S_sorted[i]
            # Добавляем элемент в подмножество и увеличиваем текущую сумму
            result = backtrack(i + 1, current_sum + num, subset + [num])
            if result is not None:
                return result
        
        return None
    
    return backtrack(0, 0, [])

# Пример использования
S = [3, 34, 4, 12, 5, 2, 1, 7]
T = 16
result = subset_sum_backtracking(S, T)

if result:
    print("Найденное подмножество:", result)
else:
    print("Нет подмножества с суммой", T)
