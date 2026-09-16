class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        left = 0
        s2_count = Counter()

        for right, char in enumerate(s2):
            s2_count[char] += 1
            
            if right - left +  1 > len(s1):
                s2_count[s2[left]] -= 1
                left += 1

            if s2_count == s1_count:
                return True
        return False
        