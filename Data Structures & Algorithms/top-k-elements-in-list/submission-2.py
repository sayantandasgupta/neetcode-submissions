import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for key in freq.keys():
            heapq.heappush(heap, (freq[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [key for _, key in heap]
        
        