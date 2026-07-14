class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        co=0
        for i in nums:
            if i==1:
                co+=1
                count=max(count,co)
            else:
                co=0
        return count
        