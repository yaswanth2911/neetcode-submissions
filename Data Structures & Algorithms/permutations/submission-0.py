class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i,nums):
            if i==len(nums):
                return [[]]
            resper=[]
            per=helper(i+1,nums)
            for p in per:
                for j in range(len(p)+1):
                    pcopy=p.copy()
                    pcopy.insert(j,nums[i])
                    resper.append(pcopy)
            return resper
        return helper(0,nums)
    
        