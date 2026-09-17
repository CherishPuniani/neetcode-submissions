class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        j = 1
        n = len(intervals)

        intervals.sort(key = lambda x: x[0])

        while i < n and j<n:
            
            if intervals[i][1] < intervals[j][0]:
                ans.append(intervals[i])
                i = j
            elif intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1],intervals[j][1])
            j+=1
            
        # i += 1
        ans.append(intervals[i])

        return ans