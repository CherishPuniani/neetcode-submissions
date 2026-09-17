class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # merge intervals and then subtract the size?

        intervals.sort(key = lambda x: x[0])

        erased = [intervals[0]]
        for s,e in intervals:
            if erased[-1][1] > s:
                erased[-1][1] = min(erased[-1][1],e)
            else:
                erased.append([s,e])

        return len(intervals) - len(erased)
