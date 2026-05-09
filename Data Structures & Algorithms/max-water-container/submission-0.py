class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = 0
        i = 0
        j = len(heights) - 1
        while i <  j:
            h =  (j - i) * min (heights[i], heights[j])
            maxH = max(maxH, h)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxH
