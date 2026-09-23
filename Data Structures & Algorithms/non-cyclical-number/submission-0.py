class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def dig_squared(n):
            digits = []
            
            while n > 0:
                digits.append(n%10)
                n = int(n/10)

            s = 0
            for d in digits:
                s += d**2
            
            return s
        
        while n != 1:
            n = dig_squared(n)
            if n in seen:
                return False
            else:
                seen.add(n)
            
        return True