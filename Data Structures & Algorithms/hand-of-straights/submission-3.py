from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        frequency_map = Counter(hand)

        for cur_num in sorted(frequency_map):
            while frequency_map[cur_num] > 0:
                for num_add in range(cur_num, cur_num + groupSize):
                    if frequency_map[num_add] == 0:
                        return False

                    frequency_map[num_add] -= 1

        return True