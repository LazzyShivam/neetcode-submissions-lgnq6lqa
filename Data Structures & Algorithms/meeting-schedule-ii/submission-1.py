"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x : x.start)

        h = []
        
        heapq.heappush(h,intervals[0].end)

        for i in intervals[1:]:
            if h[0] <= i.start:
                heapq.heappop(h)
            heapq.heappush(h,(i.end))
        return len(h)    


                       