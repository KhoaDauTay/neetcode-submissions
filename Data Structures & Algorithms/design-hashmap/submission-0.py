class MyHashMap:

    def __init__(self):
        self.result = {}

    def put(self, key: int, value: int) -> None:
        self.result.update({key:value})
        

    def get(self, key: int) -> int:
        return self.result.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.result:
            del self.result[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)