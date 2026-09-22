class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set() #what all valid index do we have at hand

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2]>target[2]:
                continue
            for i in range(3):
                if t[i] == target[i]:
                    valid.add(i)
            if len(valid) == 3:
                return True

        return len(valid) == 3