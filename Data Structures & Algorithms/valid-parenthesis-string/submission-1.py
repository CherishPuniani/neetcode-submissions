class Solution:
    def checkValidString(self, s: str) -> bool:
        paren_stack = []  # Stores indices of '('
        star_stack = []   # Stores indices of '*'
        
        for i, char in enumerate(s):
            if char == '(':
                paren_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:  # char == ')'
                if paren_stack:
                    paren_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        # Match remaining '(' with '*' that appear AFTER them
        while paren_stack and star_stack:
            if paren_stack[-1] > star_stack[-1]:
                return False  # '(' appears after '*'
            paren_stack.pop()
            star_stack.pop()
            
        return len(paren_stack) == 0