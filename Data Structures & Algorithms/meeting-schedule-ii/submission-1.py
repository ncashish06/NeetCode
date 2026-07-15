"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # Date Solved: 14 July 2026, Tuesday
    # Blind 75
    # Refer: codestorywithMIK. NeetCode Editorial for Approach-2: Min Heap.
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        # Approach 1: Using Line Sweep
        # Time: O(nlogn), Space: O(n) to store events in dict

        events = defaultdict(int)

        for interval in intervals:
            events[interval.start] += 1
            events[interval.end] -= 1

        result = 0
        count = 0

        for time in sorted(events):
            count += events[time]
            result = max(result, count)

        return result
        """
        # Approach 2: Using Min Heap
        # Time: O(nlogn), Space: O(n)
        intervals.sort(key=lambda x: x.start)
        heap = []  # min-heap of end times for rooms currently in use

        for interval in intervals:
            start, end = interval.start, interval.end
            # if earliest-freeing room is free by this meeting's start, reuse it
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            # occupy a room (new or reused) with this meeting's end time
            heapq.heappush(heap, end)

        # heap size = rooms simultaneously occupied at the busiest point
        return len(heap)
