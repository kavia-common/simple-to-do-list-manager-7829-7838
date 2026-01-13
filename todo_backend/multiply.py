import sys

# PUBLIC_INTERFACE
def multiply_two_numbers(a: float, b: float) -> float:
    """Multiplies two numbers and returns the product.

    Args:
        a (float): The first factor.
        b (float): The second factor.

    Returns:
        float: The product of a and b.
    """
    return a * b

# PUBLIC_INTERFACE
def main():
    """
    Entry point for multiplying two numbers.

    Reads two numbers from command-line arguments and prints their product.
    Usage: python multiply.py 2 3
    """
    if len(sys.argv) != 3:
        print("Usage: python multiply.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)
    result = multiply_two_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
