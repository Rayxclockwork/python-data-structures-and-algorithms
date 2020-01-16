class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.kvp = ['key:value']


class Hashtable:
    def __init__(self, length=4):
        self.array = [None] * length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def get(self, key):
        i = self.hash(key)
        if self.array[i] is None:
            raise KeyError()
        else:
            for key_value_pair in self.array[i]:
                if key_value_pair[0] == key:
                    return key_value_pair[1]

    def contains(self, key):
        if key in self.array:
            return True
        else:
            return False

    def add(self, key, value):
        i = self.hash(key)
        if self.array[i] is not None:
            for key_value_pair in self.array[i]:
                if key_value_pair[0] == key:
                    key_value_pair = value
                    break
            else:
                self.array[i].append([key, value])
        else:
            self.array[i] = []
            self.array[i].append([key, value])
