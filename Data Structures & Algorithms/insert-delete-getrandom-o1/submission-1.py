class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val not in self.numMap:
            self.numMap[val] = 1
            self.length += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        del self.numMap[val]
        self.length -= 1
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, self.length - 1)
        return list(self.numMap.keys())[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()