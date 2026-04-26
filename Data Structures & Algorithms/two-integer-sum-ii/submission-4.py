class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start =0
        end = len(numbers) -1
        
        for i in range(1, len(numbers)):
            current_sum = numbers[start] + numbers[end]
            if current_sum == target:
                return [start + 1, end + 1]  # add 1 to both indices
            elif current_sum < target:
                start+=1    # add 1 to both indices
            else:
                end-=1

        