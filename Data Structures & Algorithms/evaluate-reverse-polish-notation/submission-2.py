import operator
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        op1 = []
        # op2 = []
        # ops = set('+', '-', '*', '/')
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for x in tokens:
            if x in ops:
                res = ops[x](op1[-2],op1[-1])
                for _ in range(2):
                    op1.pop()
                op1.append(int(res))
            else:
                op1.append(int(x))
        
        return op1[-1]
