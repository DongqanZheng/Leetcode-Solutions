from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_index = deque ()
        result = []

        for i in range(len(nums)):
            while max_index and max_index[0]  < i - k + 1:
                max_index.popleft()
            
            while max_index and nums[max_index[-1]] < nums[i]:
                max_index.pop()
           
            max_index.append(i)
           
            if i >= k - 1:
                result.append(nums[max_index[0]])
       
        return result
        
