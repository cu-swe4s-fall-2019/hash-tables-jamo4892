import hash_functions
import sys
# Import modules.


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

    def add(self, key):
        """
        Purpose
        -------
        Adds a hash value to a hash table.

        Inputs
        ------
        Key: string
        Hash key

        Outputs
        -------
        T: array
        Hash table with [key, value] hash values.
        """
        hash_slot = self.hash_function(key, self.N)
        # Find the value of the hash key using the
        # selected hash function.
        print(hash_slot)

        for i in range(self.N):
            # Loop over the whole hash table.

            test_slot = (hash_slot + i) % self.N
            # Test if the hash slot is empty.

            if self.T[test_slot] is None:
                self.T[test_slot] = (key, hash_slot)
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
        None. If an empty hash slot exists, the (key, value) pair is
        inserted into the hash table.
        """
        hash_slot = self.hash(key, self.N)
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
    def __init__(self, N, hash_fucntion):
        self.hash_function = hash_function
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        pass


if __name__ == '__main__':
    ht = LinearProbe(25, hash_functions.h_ascii)
    ht.add('humunuku')
    print(ht.T)
