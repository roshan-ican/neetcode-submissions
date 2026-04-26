class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # given s and k
        # remove the dups like k chars
        # so we make a hash_map
        #  we get the counts of each
        # if any count of chars are there that match with the k we remove


        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        result = []
        for char, count in stack:
            result.append(char * count)


        return "".join(result)