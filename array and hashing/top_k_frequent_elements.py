class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        min_heap, res = [], []
        for i in nums:
            d[i] += 1
        for i in d:
            heapq.heappush(min_heap, (d[i], i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        for i in min_heap:
            res.append(i[1])
    
        return res