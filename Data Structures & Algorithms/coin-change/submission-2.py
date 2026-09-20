class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {} # this maps amount to min count

        def help(amt):
            if amt == 0:
                return 0

            if amt < 0:
                return float('inf')
            if amt in memo:
                return memo[amt]

            ans = float('inf')

            for coin in coins:
                ans = min(help(amt-coin)+1, ans)
            
            memo[amt] = ans
            return ans

        ans = help(amount)

        return -1 if ans == float("inf") else ans