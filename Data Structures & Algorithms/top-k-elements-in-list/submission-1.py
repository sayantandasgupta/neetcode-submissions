import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = [(0, 0)] * k
        heapq.heapify(heap)

        for key, value in freq.items():
            if value >= heap[0][1]:
                heapq.heappop(heap)
                heapq.heappush(heap, (key, value))

        return [key for key, _ in heap]
        