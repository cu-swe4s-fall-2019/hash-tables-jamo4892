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

    try:
        key_test = len(key)
    except TypeError:
        print('Key is not a string')
        sys.exit(1)
    try:
        n_test = int(N)
    except TypeError:
        print('N is not an integer')
        sys.exit(1)
    # Check that inputs are the correct type.

    s = 0
    for i in range(len(key)):
        s += ord(key[i])

    return s % N
    # Sum the ASCII character values modulo the hash table size.


def h_rolling(key, N):
    """
    Purpose
    -------
    This function returns the rolling polynomial sum of the
    ASCII values of each element of an input string.

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

    try:
        key_test = len(key)
    except TypeError:
        print('Key is not a string')
        sys.exit(1)
    try:
        n_test = int(N)
    except TypeError:
        print('N is not an integer')
        sys.exit(1)
    # Check that inputs are the correct type.

    s = 0

    p = 53
    m = 2**64
    # Rolling polynomial values taken from lecture code.

    for i in range(len(key)):
        s += ord(key[i]) * p**i
        s = s % m
    return s % N
    # Sum the ASCII character values with the rolling polynomial
    # modulo the hash table size.


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
                        required=False)
    parser.add_argument('--method', type=str, help='Hash method',
                        required=True)
    args = parser.parse_args()
    # Add & define function arguments.

    if args.method == 'ascii':
        print(h_ascii(args.input, args.size))
    if args.method == 'rolling':
        print(h_rolling(args.input, args.size))
