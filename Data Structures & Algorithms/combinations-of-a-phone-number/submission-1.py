class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans= [""]
        digitToChar = {
                        "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "qprs",
                        "8": "tuv",
                        "9": "wxyz",
                        }

        for digit in digits:
            tmp = []
            for char in digitToChar[digit]:
                for currStr in ans:
                    tmp.append(currStr + char)

            ans = tmp
        
        return ans