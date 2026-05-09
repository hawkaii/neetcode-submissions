class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)
        return sorted_keys[:k]
