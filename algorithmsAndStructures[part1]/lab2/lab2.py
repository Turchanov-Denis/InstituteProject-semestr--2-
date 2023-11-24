class ExpressionEvaluator:
    def __init__(self):
        self.stack = []

    def is_operator(self, char):
        return char in {'+', '-', '*', '/'}

    def perform_operation(self, operator):
        operand2, operand1 = self.stack.pop(), self.stack.pop()
        if operator == '+': self.stack.append(operand1 + operand2)
        elif operator == '-': self.stack.append(operand1 - operand2)
        elif operator == '*': self.stack.append(operand1 * operand2)
        elif operator == '/': self.stack.append(operand1 / operand2)

    def evaluate_expression(self, expression):
        for char in expression:
            if char.isdigit(): self.stack.append(int(char))
            elif char == '(': self.stack.append(char)
            elif char == ')':
                while self.stack[-1] != '(': self.perform_operation(self.stack.pop())
                self.stack.pop()
            elif self.is_operator(char):
                while self.stack and self.stack[-1] in {'+', '-', '*', '/'} and char in {'+', '-'}:
                    self.perform_operation(self.stack.pop())
                self.stack.append(char)
            elif char == '=':
                while self.stack and self.stack[-1] in {'+', '-', '*', '/'}:
                    self.perform_operation(self.stack.pop())
        return self.stack[0]

    def run(self):
        expression = input("Enter a mathematical expression ending with '=': ")
        result = self.evaluate_expression(expression)
        print(f"Result: {result}")


if __name__ == "__main__":
    expression_evaluator = ExpressionEvaluator()
    expression_evaluator.run()
