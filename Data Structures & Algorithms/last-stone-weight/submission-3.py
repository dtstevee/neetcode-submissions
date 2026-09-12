class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = -heapq.heappop(stones)
            stone_2 = -heapq.heappop(stones)
            diff = stone_1 - stone_2

            if diff > 0:
                heapq.heappush(stones, -diff)
        
        return - stones[0] if stones else 0

