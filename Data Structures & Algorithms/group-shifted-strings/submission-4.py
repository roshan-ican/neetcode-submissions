class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # have a to z 
        c = {}
        for item in strings:
            signature = []
            for i in range(1, len(item)):
                diff = (ord(item[i]) - ord(item[i-1])) % 26
                signature.append(diff)

            signature = tuple(signature)
            # for i in strings:
            #     if signature not in c:
            #         c[signature] = []
            # c[signature].append(item)
            if signature not in c:
                c[signature] = []
            c[signature].append(item)
        return list(c.values())

        print(c)

        
         
        
