class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        if s == t:
            return True
        s_set = set()
        t_set = set()

        for n in s:
            s_set.add(n)

        for n in t:
            t_set.add(n)
        print(s_set)
        print(t_set)
        if s_set==t_set:
            return False
     

        return len(s_set) == len(t_set)

        