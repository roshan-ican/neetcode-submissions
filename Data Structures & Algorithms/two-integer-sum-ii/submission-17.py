class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         add = numbers[i] + numbers[j]
        #         if add == target:
        #             return [i + 1 , j + 1]

        i  = 0 
        j = len(numbers) - 1

        while i <= j:
            add = numbers[i] + numbers[j]
            if add == target:
                return [i + 1, j + 1]
            elif add < target:
                i += 1
            else:
                j -= 1
        return []

            


        