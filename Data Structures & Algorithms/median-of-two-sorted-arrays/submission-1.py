class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        n = len(arr)
        arr.sort()
        mid = math.floor(n / 2)

        if n % 2 != 0:
            return arr[mid]
        return (arr[mid - 1] + arr[mid]) / 2