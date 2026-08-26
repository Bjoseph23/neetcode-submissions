class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}

        for num in nums:
            count[num] = count.get(num, 0) +1
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))
        return [h[1] for h in heap]

