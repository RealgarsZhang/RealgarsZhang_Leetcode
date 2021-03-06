# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda I:I.start)
        
        n = len(intervals)
        for i in range(n-1):
            if intervals[i].end>intervals[i+1].start:
                return False
        return True
        
