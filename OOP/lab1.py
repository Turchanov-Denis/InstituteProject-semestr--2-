# Турчанов Денис \ ПМ4 Адмо \  Лабораторная 1

import math

class NumericalIntegration:
    def __init__(self, function, a, b, n):
        self.function = function  
        self.a = a  
        self.b = b  
        self.n = n  

    def calculate(self):
        pass  

class TrapezoidalIntegration(NumericalIntegration):
    def calculate(self):
        h = (self.b - self.a) / self.n
        integral = (h / 2) * (self.function(self.a) + 2 * sum(self.function(self.a + i * h) for i in range(1, self.n)) + self.function(self.b))
        return integral, h, self.n

class ParabolicIntegration(NumericalIntegration):
    def calculate(self):
        if self.n % 2 == 1:
            raise ValueError("The number of points must be even for parabolic integration.")
        
        h = (self.b - self.a) / self.n
        integral = (h / 3) * (self.function(self.a) + 4 * sum(self.function(self.a + i * h) for i in range(1, self.n, 2)) + 2 * sum(self.function(self.a + i * h) for i in range(2, self.n - 1, 2)) + self.function(self.b))
        return integral, h, self.n


if __name__ == "__main__":
    def test_function(x):
        return x**2  

    a = 0
    b = 1
    n = 1000  

    trapezoidal_integration = TrapezoidalIntegration(test_function, a, b, n)
    result_trap, h_trap, n_trap = trapezoidal_integration.calculate()

    parabolic_integration = ParabolicIntegration(test_function, a, b, n)
    result_parab, h_parab, n_parab = parabolic_integration.calculate()

    print(f"Trapezoidal Integration Result: {result_trap}")
    print(f"Step size for Trapezoidal Integration: {h_trap}")
    print(f"Number of points used for Trapezoidal Integration: {n_trap}\n")

    print(f"Parabolic Integration Result: {result_parab}")
    print(f"Step size for Parabolic Integration: {h_parab}")
    print(f"Number of points used for Parabolic Integration: {n_parab}")
