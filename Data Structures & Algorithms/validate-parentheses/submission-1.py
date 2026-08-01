class Solution:
    def isValid(self, s: str) -> bool:
        hash={'}':'{',']':'[',')':'('}
        stack=[]
        for i in s:
            if i in hash:
                if stack and stack[-1]==hash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False