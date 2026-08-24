class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elems = set()

        l=0
        r=0
        ans = 0
        while r < len(s):
            if s[r] in elems:
                elems.remove(s[l])
                l += 1
            else:
                elems.add(s[r])
                ans = max(r-l+1, ans)
                r += 1
                

        return ans