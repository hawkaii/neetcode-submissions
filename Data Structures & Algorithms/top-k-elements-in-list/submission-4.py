class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            for x in nums:
                count[x] = count.get(x, 0) + 1
            return sorted(count, key=count.get, reverse=True)[:k]

        