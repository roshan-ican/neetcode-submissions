class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countA = {}
        countB = {}

        for n in s:
            countA[n] = countA.get(n, 0) + 1
        for n in t:
            countB[n] = countB.get(n, 0) + 1

        return countA == countB
    