class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):

            l = i + 1
            r = len(nums) - 1

            while l < r:

                cur_sum = nums[i] + nums[l] + nums[r] 
                if cur_sum == 0:
                    ans.add((nums[i] , nums[l] , nums[r] ) )
                    l += 1
                    r -= 1
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
        return list(ans)
