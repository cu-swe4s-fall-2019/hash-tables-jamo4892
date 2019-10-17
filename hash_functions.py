import sys
import argparse
# Import modules


def h_ascii(key, N):
    """
    Purpose
    -------
    This function returns the sum of the ASCII values of each
    element of an input string.

    Inputs
    ------
    Key: string
    String of ASCII characters

    N: integer
    Size of hash table

    Outputs
    -------
    Hash: integer
    Sum of the ASCII character values modulo the hash table size
    """

    s = 0
    for i in range(len(key)):
        try:
            key_test = str(key)
        except ValueError:
            print('Key is not a string')
            sys.exit(1)
        try:
            n_test = int(N)
        except ValueError:
            print('N is not an integer')
            sys.exit(1)
        # Check that inputs are the correct type.

        s += ord(key[i])

    return s % N
    # Sum the ASCII character values modulo the hash table size.


def h_rolling(key, N):
    return None


if __name__ == '__main__':
    """
    This is the main function. It calls the
    h_ascii and h_rolling functions above.
    """

    parser = argparse.ArgumentParser(description='Hash Functions',
                                     prog='hash_functions.py')

    parser.add_argument('--input', type=str,
                        help='Input file/string', required=True)
    parser.add_argument('--size', type=int, help='Hash table size',
                        required=True)
    parser.add_argument('--method', type=str, help='Hash method',
                        required=True)
    args = parser.parse_args()

    print(h_ascii(args.input, args.size))
    print(h_ascii(args.input, 'size'))
