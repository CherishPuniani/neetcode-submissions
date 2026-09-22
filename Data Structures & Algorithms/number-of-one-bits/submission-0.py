class Solution:
    def hammingWeight(self, n: int) -> int:
        binstr = bin(n)[2:]

        count = 0
        for c in binstr:
            if c == '1':
                count += 1
        
        return count