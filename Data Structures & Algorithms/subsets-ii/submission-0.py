class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset=[]
        curset=[]
        def helper(i):
            if i>=len(nums):
                subset.append(curset.copy())
                return 
            curset.append(nums[i])
            helper(i+1)
            curset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            helper(i+1)
        helper(0)
        return subset

        