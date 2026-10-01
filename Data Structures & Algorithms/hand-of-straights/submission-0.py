class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        frequency_map = Counter(hand)

        while frequency_map:
            cur_num = min(frequency_map.keys())
            cur_count = groupSize
            num_add = cur_num
            
            for _ in range(groupSize):
                if not frequency_map[num_add]:
                    return False
                
                frequency_map[num_add] -= 1
                if frequency_map[num_add] == 0:
                    del frequency_map[num_add]
                num_add += 1
        
        return True
            