# LeetCode Problem 56: Merge Intervals
# Difficulty: Medium
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Step 1: Check if intervals is empty
        if not intervals:
            return []
        
        # Step 2: Check if intervals has only one interval
        elif len(intervals) == 1:
            return intervals
        
        # Step 3: Sort intervals and merge overlapping ones
        else:
            
            # Step 3a: Initialize a list to hold merged intervals
            merged = []
            
            # Step 3b: Sort intervals based on the start time
            intervals.sort(key=lambda x: x[0])

            # Step 3c: Initialize the first interval as the previous interval
            prev = intervals[0]

            # Step 3d: Iterate through the sorted intervals and merge them
            for interval in intervals[1:]:
                
                # If the current interval overlaps with the previous one, merge them    
                if interval[0] <= prev[1]:
                    prev[1] = max(prev[1], interval[1])
                    
                # Otherwise, add the previous interval to merged and update prev
                else:
                    merged.append(prev)
                    prev = interval
            
            # Step 3e: Add the last merged interval to the list
            merged.append(prev)

            # Step 4: Return the list of merged intervals
            return merged
        
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals1 = [[5, 10], [1, 3], [4, 6]]
solution = Solution()
print(solution.merge(intervals))  # Output: [[1,6],[8,10],[15,18]]
print(solution.merge(intervals1))  # Output: [[1, 3], [4, 6], [5, 10]]

# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the merged intervals list
