class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_len = 0
        ans = ""
        for t in range(n):
            #  check for odd length
            i,j = t,t
            while i>=0 and j<n:
                if s[i] != s[j]:
                    break
                elif j-i+1 > ans_len:
                    ans = s[i:j+1]
                    ans_len = j-i+1
                i -=1
                j += 1


            # check for even length
            i,j = t,t+1
            while i>=0 and j<n:
                if s[i] != s[j]:
                    break
                elif j-i+1 > ans_len:
                    ans = s[i:j+1]
                    ans_len = j-i+1
                i -=1
                j += 1

        return ans
            

