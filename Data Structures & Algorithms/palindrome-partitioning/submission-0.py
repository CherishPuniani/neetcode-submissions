class Solution:
    def checkPalindrome(self, s) -> bool:
        i = 0
        j = len(s)-1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans, temp = [], []
        n = len(s)

        def help(i):
            if i == len(s):
                ans.append(temp[:])
                return
            
            for j in range(i, len(s)):
                if self.checkPalindrome(s[i:j+1]):
                    temp.append(s[i:j+1])
                    help(j+1)
                    temp.pop()
            
        help(0)
        return ans
