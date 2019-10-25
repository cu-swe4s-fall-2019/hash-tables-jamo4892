import hash_functions
import sys
import argparse
import random
import time
# Import modules.


def reservoir_sampling(new_val, size, V):
    """
    I think this function increases
    the size of a hash table.
    """
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val
    print(V)


class LinearProbe:
    """
    Class to search & fill a hash table via linear probing.
    """
    def __init__(self, N, hash_function):
        """
        Initialization of class parameters.
        """
        self.hash_function = hash_function
        # Set the hash function to use.

        self.N = N
        self.M = 0
        # Set table size and initial number of keys.

        self.T = [None for i in range(N)]
        # Blank [hash_key, hash_value] array.

    def add(self, key, value):
        """
        Purpose
        -------
        Adds a hash value to a hash table.

        Inputs
        ------
        Key: string
        Hash key

        Value: integer
        Value of a hash key

        Outputs
        -------
        T: array
        Hash table with [key, value] hash values.
        """
        hash_slot = self.hash_function(key, self.N)
        # Find the value of the hash key using the
        # selected hash function.

        for i in range(self.N):
            # Loop over the whole hash table.

            test_slot = (hash_slot + i) % self.N
            # Test if the hash slot is empty.

            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
            # If the hash slot is empty, put the hash value
            # in that slot.
        return False

    def search(self, key):
        """
        Purpose
        -------
        Search a hash table for a specific key.

        Inputs
        ------
        Key: string
        Hash key

        Outputs
        -------
        (Key, Value)
        Key and value associated with that key.
        """
        hash_slot = self.hash_function(key, self.N)
        # Hash value to search for.

        for i in range(self.N):
            # Loop over the whole hash table.

            test_slot = (hash_slot + i) % self.N
            # Test if the hash slot is empty.

            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
            # Test if the hash slot is empty.
        return None


class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        # Set the hash function to use.

        self.N = N
        self.M = 0
        # Set table size and initial number of keys.

        self.T = [[] for i in range(N)]
        # Blank [hash_key, hash_value] array.

    def add(self, key, value):
        """
        Purpose
        -------
        Adds a hash value to a hash table.

        Inputs
        ------
        Key: string
        Hash key

        Value: integer
        Value of a hash key

        Outputs
        -------
        T: array
        Hash table with [key, value] hash values.
        """
        hash_slot = self.hash_function(key, self.N)
        # Find the value of the hash key using the
        # selected hash function.

        self.T[hash_slot].append((key, value))
        self.M += 1
        return True
        # Put the hash value in the hash slot.

    def search(self, key):
        """
        Purpose
        -------
        Search a hash table for a specific key.

        Inputs
        ------
        Key: string
        Hash key

        Outputs
        -------
        (Key, Value)
        Key and value associated with that key.
        """
        hash_slot = self.hash_function(key, self.N)
        # Find the value of the hash key using the
        # selected hash function.

        for k, v in self.T[hash_slot]:
            if key == k:
                return v
        return None
        # Return the hash value for the chosen key.


if __name__ == '__main__':
    """
    This is the main function. It calls either the LinearProbe
    or ChainedHash classes, and their functions.
    """

    parser = argparse.ArgumentParser(description='Hash Tables',
                                     prog='hash_tables')
    parser.add_argument('--size', type=int,
                        help='Hash table size', required=True)
    parser.add_argument('--method', type=str,
                        help='ascii or rolling', required=True)
    parser.add_argument('--collision', type=str,
                        help='linear or chain', required=True)
    parser.add_argument('--input', type=str, help='File name',
                        required=True)
    parser.add_argument('--keys_add', type=int, help='Keys to add',
                        required=True)
    parser.add_argument('--keys_search', type=int, help='Keys to search',
                        required=True)
    args = parser.parse_args()

    N = args.size
    hash_algorithm = args.method
    collision_strategy = args.collision
    data = args.input
    keys_add = args.keys_add
    keys_search = args.keys_search
    # Add & define class input arguments.

    ht = None

    if hash_algorithm == 'ascii':
        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_ascii)
        if collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_ascii)
        # Run class initializer for linear or chained hashes
        # with the ascii function.

    if hash_algorithm == 'rolling':
        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_ascii)
        if collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_ascii)
    # Run class initializer for linear or chained hashes
    # with the rolling function.

    V = []
    for l in open(data):
        reservoir_sampling(l.rstrip(), keys_search, V)
        # Not sure what this function call actually does.

        t0 = time.time()
        ht.add(l.rstrip(), l.rstrip())
        t1 = time.time()
        print('add', ht.M/ht.N, t1 - t0)
        # Print the time it takes to add values
        # to the hash table.

        if ht.M == keys_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)
        # Print the time it takes to search the
        # hash table.
