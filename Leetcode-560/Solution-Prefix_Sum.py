from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        

        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]
            
            
            seen[prefix_sum] += 1
            
        
        return count
