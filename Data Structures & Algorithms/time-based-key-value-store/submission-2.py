class TimeMap:

    def __init__(self):
        self.hash_map = {}
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hash_map.get(key, [])
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            value, ts = arr[mid]
            print(mid, "_mid index")
            if ts == timestamp:
                return value
            elif ts < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        if high >= 0:
            return arr[high][0]
        return ""
        
