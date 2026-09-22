class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            if (n >> i) & 1 == 1:
                ans = ans | (1 << 31 - i)
            
        return ans