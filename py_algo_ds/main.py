"""
The main module for the project.
"""


def hello() -> str:
    """
    Function to say Hello Python

    Returns:
        str: "Hello Python!"
    """
    return "Hello Python!"


def main() -> None:
    """
    Main function to run the hello function.
    """
    print(hello())


if __name__ == "__main__":
    main()
