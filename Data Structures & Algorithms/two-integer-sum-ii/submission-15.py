class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        start = 0
        end = len(numbers) - 1

        while start != end:
            suu = numbers[start] + numbers[end]
            if suu == target:
                return [start + 1, end + 1]
            elif suu > target:
                end-=1
            else:
                start+=1
        print(start, end, "__re")
        return [start + 1, end + 1]