class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        
        for i in range(len(nums) - k + 1):

            m = -1
            for j in range(i , i + k):
                m = max(m, nums[j])
            res.append(m)

        return res



        
