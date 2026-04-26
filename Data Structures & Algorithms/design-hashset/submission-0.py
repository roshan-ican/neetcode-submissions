class MyHashSet:

    def __init__(self):
        self.hash_set = set()
        

    def add(self, key: int) -> None:
        return self.hash_set.add(key)


    def remove(self, key: int) -> None:
        return self.hash_set.discard(key)
        

    def contains(self, key: int) -> bool:
        if key in self.hash_set:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)