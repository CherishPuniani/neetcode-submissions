class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = defaultdict(int)
        for c in s1:
            dic[c] += 1
        l = 0
        while l <= len(s2) - len(s1):
            if s2[l] not in dic:
                l += 1
            else:
                s2_dic = defaultdict(int)
                for t in range(len(s1)):
                    if s2[l+t] in dic:
                        s2_dic[s2[l+t]] += 1
                    else: 
                        break
                
                if dic == s2_dic:
                    return True
                else:
                    l += 1
        
        return False
                    

