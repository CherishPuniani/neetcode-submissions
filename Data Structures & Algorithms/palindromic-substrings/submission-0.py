class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for t in range(n):
            #  check for odd length
            i,j = t,t
            while i>=0 and j<n and s[i] == s[j]:
                count += 1
                i -=1
                j += 1


            # check for even length
            i,j = t,t+1
            while i>=0 and j<n and s[i] == s[j]:
                count += 1
                i -=1
                j += 1

        return count