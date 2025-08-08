class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_of_subsequence = sum(nums[0:k]) 
        result = sum_of_subsequence/k
        for i in range(len(nums) - k):
            sum_of_subsequence -= nums[i]
            sum_of_subsequence += nums[i+k]
            avg = sum_of_subsequence/k
            if avg > result:
                result = avg

        return result
