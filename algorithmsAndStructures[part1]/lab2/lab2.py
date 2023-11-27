# class ArithmeticExpressionSolver:
#     def __init__(self):
#         pass

#     @staticmethod
#     def evaluate_expression(expression):
#         try:
#             result = eval(expression[:-1])
#             return result
#         except ZeroDivisionError:
#             return "Error: division by zero"
#         except Exception as e:
#             return f"Error: {str(e)}"

# def main():
#     expression_solver = ArithmeticExpressionSolver()

#     expression = input("Enter a mathematical expression (ending with '='): ")

#     result = expression_solver.evaluate_expression(expression)
#     print(f"Result of the expression: {result}")

# if __name__ == "__main__":
#     main()

class ArithmeticExpressionSolver:
    def __init__(self):
        pass

    @staticmethod
    def evaluate_expression(expression):
        try:
            result = ArithmeticExpressionSolver.calculate(expression[:-1])
            return result
        except ZeroDivisionError:
            return "Error: division by zero"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def calculate(expression):
        operators = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                     '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

        def shunting_yard_algorithm(tokens):
            output = []
            stack = []
            for token in tokens:
                if token.isdigit():
                    output.append(token)
                elif token in operators:
                    while (stack and stack[-1] in operators and
                           operators[token][0] <= operators[stack[-1]][0]):
                        output.append(stack.pop())
                    stack.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    if stack and stack[-1] == '(':
                        stack.pop()
            while stack:
                output.append(stack.pop())
            return output

        def calculate_rpn(rpn):
            stack = []
            for token in rpn:
                if token.isdigit():
                    stack.append(float(token))
                elif token in operators:
                    y, x = stack.pop(), stack.pop()
                    stack.append(operators[token][1](x, y))
            return stack[0]

        tokens = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
        print(tokens)
        rpn = shunting_yard_algorithm(tokens)
        result = calculate_rpn(rpn)
        return result


def main():
    expression_solver = ArithmeticExpressionSolver()

    expression = input("Enter a mathematical expression (ending with '='): ")

    result = expression_solver.evaluate_expression(expression)
    print(f"Result of the expression: {result}")

if __name__ == "__main__":
    main()

