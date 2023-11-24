def find_numbers(x):
    result = []
    for k in range(int(x**0.5) + 1):
        for l in range(int(x**0.3) + 1):
            for m in range(int(x**0.2) + 1):
                current_number = 3**k * 5**l * 7**m
                if current_number <= x:
                    result.append(current_number)
    return sorted(result)


def main():
    x = int(input("Enter a number x: "))
    numbers = find_numbers(x)
    print(f"Numbers satisfying the condition: {numbers}")


if __name__ == "__main__":
    main()
