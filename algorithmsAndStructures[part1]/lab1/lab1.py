class BracketChecker:
    def __init__(self, brackets):
        self.brackets = brackets
        self.stack = []

    def check_brackets(self, input_str):
        for char in input_str:
            if char in self.brackets:
                self.stack.append(char)
            elif char in self.brackets.values():
                if not self.stack or self.brackets[self.stack.pop()] != char:
                    return False
        return not self.stack

    def run(self):
        input_str = input(f"Enter a string using brackets {list(self.brackets.keys())} {list(self.brackets.values())}: ")
        result = "valid" if self.check_brackets(input_str) else "not valid"
        print(f"The string is {result}")


if __name__ == "__main__":
    bracket_checker_1 = BracketChecker({"(": ")"})
    bracket_checker_1.run()

    bracket_checker_2 = BracketChecker({"(": ")", "{": "}", "[": "]"})
    bracket_checker_2.run()
