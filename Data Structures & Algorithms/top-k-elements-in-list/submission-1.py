from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        res = []
        top = num_count.most_common(k)
        return [v[0] for v in top]
        