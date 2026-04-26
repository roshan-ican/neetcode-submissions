class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_map = {}

        for n in arr:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        count = 0
        for x in arr:          # keep original order
            if hash_map[x] == 1:
                count += 1
                if count == k:
                    return x
        return ""
