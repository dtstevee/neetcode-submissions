class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def total_hours(pile, k):
            count_total = 0
            for i in pile:
                count_total += (i//k)
                if i % k != 0:
                    count_total += 1
            return count_total
        
        # initialize binary search
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            count_round = total_hours(piles, mid)
            if count_round <= h:
                right = mid - 1
                continue
            else:
                left = mid + 1
            
        return left