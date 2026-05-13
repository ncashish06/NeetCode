class Solution:
    from collections import Counter
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        n = len(nums)
        for k, v in freq_map.items():
            if v > n//2:
                return k