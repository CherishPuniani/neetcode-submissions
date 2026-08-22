class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hMap = defaultdict(int)
        for n in nums:
            hMap[n] +=1
        freqList = [[] for _ in range(len(nums)+1)]

        for num, freq in hMap.items():
            freqList[freq].append(num)
        
        for t in range(len(freqList)-1, 0, -1):
            for p in freqList[t]:
                ans.append(p)
                if len(ans) == k:
                    return ans
        
        return ans

        