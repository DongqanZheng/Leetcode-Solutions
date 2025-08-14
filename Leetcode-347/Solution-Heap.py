from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = Counter(nums)
        
        heap = []
        for element, frequency in frequency_table.items():
            heapq.heappush(heap,(frequency, element))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            result.append(heapq.heappop(heap)[1]) 
        
        return result
        
