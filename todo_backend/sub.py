import sys

# PUBLIC_INTERFACE
def subtract_two_numbers(a: float, b: float) -> float:
    """Subtracts the second number from the first and returns the result.

    Args:
        a (float): The number to subtract from.
        b (float): The number to subtract.

    Returns:
        float: The result of a - b.
    """
    return a - b

# PUBLIC_INTERFACE
def main():
    """
    Entry point for subtracting two numbers.

    Reads two numbers from command-line arguments and prints their difference.
    Usage: python sub.py 5 3
    """
    if len(sys.argv) != 3:
        print("Usage: python sub.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)
    result = subtract_two_numbers(num1, num2)
    print(f"The difference between {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
