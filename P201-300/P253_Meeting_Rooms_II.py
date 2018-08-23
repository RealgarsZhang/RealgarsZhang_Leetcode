# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda item:item.start)
        time_list = []
        n = len(intervals)
        for i in range(n):
            time_list.append([intervals[i].start,0])
            time_list.append([intervals[i].end,1])
        
        time_list.sort(key = lambda item:item[0])
        
        
        res = 0
        temp_res = 0
        for time in time_list:
            if time[1] == 0:
                temp_res += 1
            else:
                res = max(res,temp_res)
                temp_res -= 1
        
        return res


