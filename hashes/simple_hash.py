"""
Simple hash is a fixed size hash that only accepts integers as keys
"""

from hash import Hash


class SimpleHash(Hash):
    def __init__(self, capacity=10):
        Hash.__init__(self, capacity)

    def put(self, key, obj):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()

    def remove(self, key):
        raise NotImplementedError()
