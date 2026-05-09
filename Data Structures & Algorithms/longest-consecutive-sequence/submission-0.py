class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = []
        for num in nums:
            if num-1 in nums:
                continue
            starts.append(num)

        res = 0
        for s in starts:
            m = 1
            i = s
            while i+1 in nums:
                m += 1
                i+=1
            res = max(res, m)

        return res
            



        
