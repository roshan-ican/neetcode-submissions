class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # l = 0
        # r = 0
        # count = 0
        # s = sorted(s)
        # s_unique = set()
        # for i in range(len(g)):
        #     for j in range(len(s)):
        #         if g[i] <= s[j] and j not in s_unique:
        #             count+=1
        #             s_unique.add(j)
        #             break
        # return count
        g = sorted(g)
        s= sorted(s)
        l =0
        r = 0
        count=0
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                l+=1
                r+=1
                count+=1
            elif s[r] < g[l]:
                r+=1
        return count




        