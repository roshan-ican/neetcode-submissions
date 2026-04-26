class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = 0
        white_count = 0
        min_ops = k
        while j < len(blocks):
            if blocks[j] == "W":
                white_count += 1
            
            if j - i + 1 == k:
                min_ops = min(min_ops, white_count)
                if blocks[i] == 'W':
                    white_count -= 1
                i += 1
            j += 1

        return min_ops