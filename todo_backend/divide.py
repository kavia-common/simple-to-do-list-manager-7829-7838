import sys

# PUBLIC_INTERFACE
def divide_two_numbers(a: float, b: float) -> float:
    """Divides the first number by the second and returns the quotient.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0.0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

# PUBLIC_INTERFACE
def main():
    """
    Entry point for dividing two numbers.

    Reads two numbers from command-line arguments and prints their quotient.
    Handles division by zero with an error message and non-zero exit code.
    Usage: python divide.py 10 2
    """
    if len(sys.argv) != 3:
        print("Usage: python divide.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)
    try:
        result = divide_two_numbers(num1, num2)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        sys.exit(2)
    print(f"The quotient of {num1} divided by {num2} is {result}")

if __name__ == "__main__":
    main()
