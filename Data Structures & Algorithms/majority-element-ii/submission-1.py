class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # freq = {}
        # n = len(nums)
        # k = n // 3
        # print(k)
        # for n in nums:
        #     if n in freq:
        #         freq[n] += 1
        #     else:
        #         freq[n] = 1
        # print(freq)
        # res = []
        # for key,val in freq.items():
        #     if val > k:
        #         res.append(key)
        #     else:
        #         continue
        # return res
        k = len(nums) // 3
    
        count1 = 0
        count2 = 0
        cand1 = cand2 = None
        for n in nums:
            if n == cand1:
                count1 +=1
            elif n == cand2:
                count2 += count2
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
                
            else:
                count1-=1
                count2-=1
        res  = []
        n = len(nums)
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > k:
                res.append(cand)
        return res
    