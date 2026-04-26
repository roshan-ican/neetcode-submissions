class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # keep track of s and t yani the letters are not there in the s of t then we don't increase t count
        # and else we combine both tracker at the end

        s_track = 0
        t_track = 0

        # if t in s and len(t) == 1:
        #     return 0
        # if s not in t:
        #     return len(t)

        while s_track < len(s) and t_track < len(t):
            if s[s_track] == t[t_track]:
                t_track += 1
                s_track += 1
            else:
                s_track += 1
        print(t_track)
            
        return len(t) - t_track
            
            
        
        # # for i in range(len(s)):
        # #     if s[i] not in t:
        # #         s_track += 1
        
        # res = s_track + t_track
        # return res

        