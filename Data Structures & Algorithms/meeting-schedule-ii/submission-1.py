"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda x: x.start)

        heap = [intervals[0].end]
        ans = len(heap)

        # create a priority queue of meetings
        for meet in intervals[1:]:
            if meet.start < heap[0]:
                heapq.heappush(heap,meet.end)
                ans = max(ans,len(heap))
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,meet.end)

            

        return ans
