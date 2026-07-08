class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums) * 2
        ans = []
        j = 0
        for i in range(l):
            if i % len(nums) == 0:
                j = 0
            ans.append(nums[j])
            j += 1
        
        return ans
