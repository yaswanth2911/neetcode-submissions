class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arr = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            arr.append(sorted_freq[i][0])
        return arr