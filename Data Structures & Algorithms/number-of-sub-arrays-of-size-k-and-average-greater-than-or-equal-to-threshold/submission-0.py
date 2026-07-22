class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        window=sum(arr[:k])
        if window//k>=threshold:
            count+=1
        for r in range(k,len(arr)):
            window+=arr[r]
            window-=arr[r-k]
            if window//k>=threshold:
                count+=1
        return count
        