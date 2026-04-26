import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(low, high):
            pivot_idx = random.randint(low, high)
            nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]

            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        def quickSort(low, high):
            if low < high:
                pi = partition(low, high)
                quickSort(low, pi - 1)
                quickSort(pi + 1, high)

        quickSort(0, len(nums) - 1)
        return nums
