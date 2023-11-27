class PrimeFactorsCombinations:
    def __init__(self, x):
        self.x = x

    def find_combinations(self):
        combinations = []

        for k in range(0, self.x + 1):
            for l in range(0, self.x + 1):
                for m in range(0, self.x + 1):
                    if 3**k * 5**l * 7**m == self.x:
                        combinations.append((k, l, m))

        return combinations

    def get_combinations(self):
        return self.find_combinations()


def main():
    x_input = int(input("Enter the number x: "))

    prime_factors = PrimeFactorsCombinations(x_input)
    combinations = prime_factors.get_combinations()

    if combinations:
        print(combinations)
    else:
        print(f"The number {x_input} cannot be represented as a product of powers of 3, 5, and 7.")


if __name__ == "__main__":
    main()
