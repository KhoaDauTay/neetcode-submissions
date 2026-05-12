class MyHashSet:

    def __init__(self):
        self.result = {}

    def add(self, key: int) -> None:
        if key not in self.result:
            self.result[key] = 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.result[key]
        

    def contains(self, key: int) -> bool:
        return key in self.result


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)