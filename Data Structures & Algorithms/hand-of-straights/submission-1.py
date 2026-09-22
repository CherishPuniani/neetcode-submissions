class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hmap = defaultdict(int)
        for i in hand:
            hmap[i] += 1
        
        for key in sorted(hmap):
            count = hmap[key]
            if count > 0:
                for i in range(groupSize):
                    if hmap[key + i] < count:
                        return False
                    hmap[key + i] -= count
        
        return True
