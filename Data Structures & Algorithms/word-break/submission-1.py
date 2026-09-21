class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1) # if we can reach till i with a word
        dp[0] = True 

        for i in range(n):
            for word in wordDict:
                if s[i:i+len(word)] == word and dp[i] == True:
                    dp[i+len(word)] = True
                

        return dp[n]

