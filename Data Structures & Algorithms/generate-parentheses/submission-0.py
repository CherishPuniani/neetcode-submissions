class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []

        # if open < n i can add open
        # if close < open i can add close
        # stop when close == open

        def help(openC, closeC):
            if openC == closeC == n:
                ans.append("".join(temp))
                return
            
            if openC < n:
                temp.append("(")
                help(openC+1, closeC)
                temp.pop()
            
            if closeC < openC:
                temp.append(")")
                help(openC, closeC+1)
                temp.pop()

        help(0,0)
        return ans

        