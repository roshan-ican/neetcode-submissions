class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        left = 0
        right = len(values) - 1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            value, stored_timestamp = values[mid] 
            
            if stored_timestamp <= timestamp:
                ans = value
                left = mid + 1
            else:
                right = mid - 1
        return ans