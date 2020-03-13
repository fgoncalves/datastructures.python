from .hash import Hash


class AnyKeyHash(Hash):
    """
    Any key hash is a fixed size hash that accepts any type of key
    """

    def __init__(self, capacity=10):
        Hash.__init__(self, capacity)

    def put(self, key, obj):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()

    def remove(self, key):
        raise NotImplementedError()
