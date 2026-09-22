class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        occ = defaultdict(list)
        for char in s:
            if char not in occ:
                occ[char] = [s.find(char),s.rfind(char)]
        n = len(s)
        ans = []
        r = l = 0

        while r < n:
            reach = occ[s[r]][1]
            # r = reach
            while r < reach:
                reach = max(reach,occ[s[r]][1])
                r += 1
            ans.append(r-l+1)
            r = reach+1
            l = r
        
        return ans
        