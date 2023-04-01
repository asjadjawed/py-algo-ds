"""
Module for demonstrating array data structures and data interpretation.
Underlying data in arrays can be interpreted differently depending on how it's read.
"""

from array import array as arr

# Create an array of integers
integer_array = arr('i', [1, 2, 3])

# Create a bytearray object from the string "Hello, World" using utf-8 encoding
buffer = bytearray("Hello Python", "utf-8")

# Create two array objects with different types (byte and float) and populate them from the buffer
byte_array = arr('b')
byte_array.frombytes(buffer)

float_array = arr('f')
float_array.frombytes(buffer)


def main():
    """
    Main Function
    """
    print(buffer)
    print(buffer.decode("utf-16"))
    print(byte_array[0])
    print(float_array[1])

    # Little Endian vs Big Endian
    print(f'integer_array in bytes: {integer_array.tobytes()}')
    integer_array.byteswap()
    print(f'integer_array in bytes after byteswap: {integer_array.tobytes()}')


if __name__ == "__main__":
    main()
