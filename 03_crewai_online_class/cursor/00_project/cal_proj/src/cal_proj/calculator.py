#!/usr/bin/env python3

class Calculator:
    def add(self, x: float, y: float) -> float:
        return x + y

    def subtract(self, x: float, y: float) -> float:
        return x - y

    def multiply(self, x: float, y: float) -> float:
        return x * y

    def divide(self, x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main() -> None:
    calc = Calculator()
    print("Simple Calculator using a Class with type hints")
    print("Enter your calculation in the format: number operator number (e.g., 2 + 3)")
    print("Supported operators: +, -, *, /")
    print("Type 'exit' or 'quit' to end the program\n")
    
    while True:
        user_input = input("Calculation: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input format. Please try again.")
                continue

            a_str, op, b_str = parts
            a, b = float(a_str), float(b_str)
            if op == '+':
                result = calc.add(a, b)
            elif op == '-':
                result = calc.subtract(a, b)
            elif op == '*':
                result = calc.multiply(a, b)
            elif op == '/':
                result = calc.divide(a, b)
            else:
                print("Unsupported operator:", op)
                continue

            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()
