class Solution:
    def climbStairs(self, n: int) -> int:

        mem = { 0:1, 1:1}
        def help(x):
            if x in mem:
                return mem[x]
            else:
                mem[x] = help(x-1) + help(x-2)
                return mem[x]
        
        return help(n)
