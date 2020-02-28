class Hash:

    def __init__(self, capacity=10):
        self.size = 0
        self.capacity = capacity

    def put(self, key, obj):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()

    def remove(self, key):
        raise NotImplementedError()
