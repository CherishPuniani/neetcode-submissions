class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i,temp in enumerate(temperatures): # I did not know about this start
            # if stack:
            # My code was failing at checking stack[-1] coz after pop there was no check
            while stack and temp > stack[-1][1]:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i,temp))
        if stack: 
            for tup in stack:
                ans[tup[0]] = 0
            
        return ans
        