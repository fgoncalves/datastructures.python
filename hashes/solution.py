"""
This file contains a solution where the hash is backed by a list.

The idea is to create a hashing function that returns indexes for the list.

When the hash is at 75% capacity, it will resize and rehash.

When there's a collision the hash will resize and rehash.

It only accepts strings as keys
"""

from hash import Hash


class HashEntry:
    """
    A class that holds 2 values - the key and the value the key points to.

    The idea is to put entries in the list.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'{self.key} -> {self.value}'


class HashBackedByList(Hash):
    def __init__(self, capacity=10):
        Hash.__init__(self, capacity)
        self.entries = self._new_entries()

    def put(self, key, value):
        """
        associate the key with the given value
        """
        # first we resize and rehash as long as the key produces a collision
        while self._is_collision(key):
            self._resize()
            self._rehash()

        index = self._hash(key)

        if self.entries[index] == None:
            self.size += 1

        self.entries[index] = HashEntry(key, value)

        # let's also resize and rehash if the hash is at 75% capacity
        if float(self.size) / float(self.capacity) >= .75:
            self._resize()
            self._rehash()

    def get(self, key):
        """
        get will return the value for the given key.

        None will be returned if there's no value
        """
        return self.entries[self._hash(key)].value

    def remove(self, key):
        """
        remove the value associated with the given key
        """
        index = self._hash(key)
        if self.entries[index] != None:
            self.size -= 1

        self.entries[index] = None

    def _hash(self, key):
        """
        return an index for the give key. This method guarantees that the index is within bounds.

        This method doesn't care if the hash needs resizing
        """
        result = 0
        for c in key:
            result += ord(c)

        result *= 31

        return result % self.capacity

    def _resize(self):
        """
        _resize will double the hash capacity and append `capacity` more entries to the hash.

        These entries will be initialized to None.

        The current entries remain in the same position.
        """
        # add as many None entries as the current capacity
        self.entries += [None] * self.capacity
        # now double the capacity
        self.capacity *= 2

    def _rehash(self):
        old_entries = filter(lambda x:  x, self.entries)

        self.entries = self._new_entries()
        self.size = 0

        for entry in old_entries:
            self.put(entry.key, entry.value)

    def _is_collision(self, key):
        # A collision happens when 2 objects have the same hash a.k.a. index, but different keys.
        entry = self.entries[self._hash(key)]
        return entry != None and entry.key != key

    def __str__(self):
        result = f'[size={self.size}, capacity={self.capacity}]\n'
        for entry in self.entries:
            result += f'{entry}\n'
        return result

    def _new_entries(self):
        return [None] * self.capacity


if __name__ == "__main__":
    h = HashBackedByList()

    h.put("foo", "bar")
    print(f'{h}')
    h.put("foo", "bar")
    print(f'{h}')
    h.put("foo", "baz")
    print(f'{h}')
    print(h.get('foo'))

    h.put("abc", "baz")
    print(f'{h}')

    h.remove("abc")
    print(f'{h}')
