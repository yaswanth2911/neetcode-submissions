class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        freq1={}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for j in t:
            if j not in freq1:
                freq1[j]=1
            else:
                freq1[j]+=1
        if freq==freq1:
            return True
        
        return False

        