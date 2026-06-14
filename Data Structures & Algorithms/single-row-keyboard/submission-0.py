class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        fingerIndex = {}
        res = 0
        for i,n  in enumerate(keyboard):
            fingerIndex[n] = i
        current_pos = 0
        for i in range(len(word)):
            targetP = word[i]
            if targetP in fingerIndex:
                target_idx = fingerIndex[targetP]

                res += abs(target_idx - current_pos)
                current_pos = target_idx
        return res

        

        