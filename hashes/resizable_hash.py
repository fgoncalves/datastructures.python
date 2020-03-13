from .hash import Hash


class ResizableHash(Hash):
    """
    Resizable hash is a hash that resizes itself every time there's a collision.

    It only accepts integers as keys
    """

    def __init__(self, capacity=10):
        Hash.__init__(self, capacity)

    def put(self, key, obj):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()

    def remove(self, key):
        raise NotImplementedError()
