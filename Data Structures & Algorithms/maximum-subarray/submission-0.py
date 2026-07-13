class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        curr=0
        for u in nums:
            curr=max(curr,0)
            curr+=u
            maxsum=max(maxsum,curr)
        return maxsum