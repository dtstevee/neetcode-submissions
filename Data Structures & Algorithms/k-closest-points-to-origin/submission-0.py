class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []

        for i in points:
            euc_dis = -(i[0]**2 + i[1]**2)
            heapq.heappush(heap, (euc_dis, i[0], i[1]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            pop = heapq.heappop(heap)
            result.append([pop[1],pop[2]])
        
        return result

 