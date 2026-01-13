import sys

# PUBLIC_INTERFACE
def add_two_numbers(a: float, b: float) -> float:
    """Adds two numbers and returns the sum.

    Args:
        a (float): The first number to add.
        b (float): The second number to add.

    Returns:
        float: The sum of a and b.
    """
    return a + b

# PUBLIC_INTERFACE
def main():
    """
    Entry point for adding two numbers.

    Reads two numbers from command-line arguments and prints their sum.
    Usage: python main.py 2 3
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)
    result = add_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
