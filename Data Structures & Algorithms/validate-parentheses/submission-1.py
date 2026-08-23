class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)

            elif char == ')':
                if stack:
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                else:
                    return False

            elif char == ']':
                if stack:
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                else:
                    return False

            elif char == '}':
                if stack:
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
                