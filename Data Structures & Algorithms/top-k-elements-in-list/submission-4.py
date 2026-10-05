class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        
        for num, cnt in count.items():
            heap.append([cnt, num])
        
        heap.sort()
        res = []

        while len(res) < k:
            res.append(heap.pop()[1])
        
        return res


        
        