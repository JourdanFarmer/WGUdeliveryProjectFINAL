# Jourdan Farmer, ID: 011503932$

class HashTable:

    # constructor
    # time complexity: O(1)
    # space complexity: O(1)
    def __init__(self):
        self.size = 128
        self.table = [None] * self.size
        self.length = -1

    # calculates index within array
    # time complexity: O(n)
    # space complexity: O(1)
    def index(self, input):
        raw_hash = 0
        input = str(input)
        for c in input:
            raw_hash += ord(c)
        return raw_hash % self.size

    # get function
    # time complexity: O(n)
    # space complexity: O(1)
    def get(self, key):
        # calculates hash value
        hash = self.index(key)
        if self.table[hash] is not None:
            for keyValuePair in self.table[hash]:
                if keyValuePair[0] == key:
                    return keyValuePair[1]
        return None

    # add function
    # time complexity: O(n)
    # space complexity: O(1)
    def add(self, key, val):
        hash = self.index(key)
        value = [key, val]
        if self.table[hash] is None:
            self.table[hash] = list([value])
            self.length += 1
        else:
            for keyValuePair in self.table[hash]:
                if keyValuePair[0] == key:
                    keyValuePair[1] = val
                    return True
                self.table[hash].append(value)
                self.length += 1
                return True

    # delete function
    # time complexity: O(n)
    # space complexity: O(1)
    def delete(self, key):
        hash = self.index(key)

        if self.table[hash] is None:
            return False

        for i in range(0, len(self.table[hash])):
            if self.table[hash][i][0] == key:
                self.table[hash].pop(i)
                self.length -= 1
                return True

    # print function
    # time complexity: O(n)
    # space complexity: O(1)
    def print(self, key):
        hash = self.index(key)
        for i in range(0, len(self.table[hash])):
            if self.table[hash][i][0] == key:
                print(self.table[hash][0][1])
