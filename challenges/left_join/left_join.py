class Hashtable:
    def __init__(self, length=4):
        self.array = [None] * length

    def hashing(self, key):
        length = len(self.array)
        return hash(key) % length

    def get(self, key):
        i = self.hashing(key)
        print(self.array)
        if self.array[i] is None:
            raise KeyError()
        else:
            for key_value_pair in self.array[i]:
                if key_value_pair[0] == key:
                    return key_value_pair[1]

            raise KeyError()


    def contains(self, key):
        i = self.hashing(key)
        if self.array[i] is None:
            return False
        else:
            for key_value_pair in self.array[i]:
                if key_value_pair[0] == key:
                    return True
            return False

    def add(self, key, value):
        i = self.hashing(key)
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



hash_1 = Hashtable()
hash_2 = Hashtable()
def left_join(hash_1, hash_2, key):
	results = []
	while key in hash_1:
		if key in hash_2:
			
			output_1 = [key, hash_1[key], hash_2.get(key)]
			results.append(output_1)
		else:
			output_2 = [key, hash_1[key], None]
			results.append(output_2)
	return results
