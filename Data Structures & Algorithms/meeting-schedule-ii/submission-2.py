"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # everytime a meet ends reduce the count and everytime a meet starts increase int

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        ans = 0
        curr = 0
        s=0
        e = 0

        while s< len(start):
            if start[s] < end[e]:
                curr += 1
                s += 1
            else:
                curr -= 1
                e += 1
            ans = max(ans,curr)

        return ans