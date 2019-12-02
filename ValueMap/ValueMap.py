class ValueMap:

    def __init__(self, parent=None):
        self._data = dict()
        self._parent = parent

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        if self._parent is not None:
            return self._parent[key]
        raise KeyError(f"Key {key} is not found")

    def __setitem__(self, key, value):
        self._data[key] = value
