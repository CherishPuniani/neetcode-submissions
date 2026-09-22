class Solution:
    def checkValidString(self, s: str) -> bool:
        # Greedy approach = keep track of max open and min open
        maxi = 0
        mini = 0
        for char in s:
            if char == '(':
                mini += 1
                maxi += 1
            elif char == ')':
                mini -= 1
                maxi -= 1
            elif char == '*':
                maxi += 1
                mini -= 1
            
            if maxi < 0:
                return False
            
            mini = max(mini,0)

        return mini == 0
