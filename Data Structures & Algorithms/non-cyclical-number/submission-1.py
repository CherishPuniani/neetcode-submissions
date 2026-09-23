class Solution:
    def isHappy(self, n: int) -> bool:
        def dig_squared(num):
            s = 0
            while num > 0:
                s += (num % 10) ** 2
                num //= 10
            return s

        slow = n
        fast = dig_squared(n)

        while fast != 1 and slow != fast:
            slow = dig_squared(slow)
            fast = dig_squared(dig_squared(fast))

        return fast == 1