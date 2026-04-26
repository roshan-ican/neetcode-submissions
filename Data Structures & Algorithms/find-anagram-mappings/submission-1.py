class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx2 = {}
        res = []
        for i, n in enumerate(nums2):
            idx2[n] = i
        """
        # For each i in nums1, look up where nums1[i] 
        appears in nums2 using idx2
        """

        for i in range(len(nums1)):
            res.append(idx2[nums1[i]])

        return res
