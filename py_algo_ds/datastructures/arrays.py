"""
Module for array data structures
"""

from array import array as arr

# Example of an array (this is actually a list in Python)
a = [1, 2, 3]

# b is an array of 3 elements
b = arr('i', [1, 2, 3])


def main():
    """
    Main Function
    """
    print(f'b in bytes: {b.tobytes()}')
    b.byteswap()
    print(f'b in bytes after byteswap: {b.tobytes()}')


if __name__ == "__main__":
    main()
