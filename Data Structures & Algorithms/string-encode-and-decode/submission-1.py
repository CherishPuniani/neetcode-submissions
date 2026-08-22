class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "1111"
        ans_str = strs[0]

        for i in range(1,len(strs)):
            ans_str = ans_str + "->" + strs[i]
        return ans_str

    def decode(self, s: str) -> List[str]:
        if s == "1111": 
            return []
        ans = []
        tempStr = ""
        i = 0
        while i < len(s):
            if s[i] == "-" and s[i+1] == ">":
                i +=2
                ans.append(tempStr)
                tempStr = ""
            else:
                tempStr += s[i]
                i += 1
        ans.append(tempStr)
        return ans
