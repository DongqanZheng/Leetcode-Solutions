from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {'(':')', '[':']', '{':'}'}

        for i in range(len(s)):
            if s[i] in mapping:
                stack.append(s[i])
            else:
                if stack:
                    left = stack.pop()
                    if mapping[left] != s[i]:
                        return False
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
