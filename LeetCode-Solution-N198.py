from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Step 1: Check if the input list is empty or has only one element.
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Step 2: Initialize two variables to store previous results
        # prev2 represents dp[i-2] → max amount if we rob up to the house before the previous one
        # prev1 represents dp[i-1] → max amount if we rob up to the previous house
        prev2 = 0        
        prev1 = nums[0]

        # Step 3: Iterate through the list starting from the second house
        for i in range(1, len(nums)):
            
            # Step 4: 
            # Either:
            # 1. Rob the current house and add its value to prev2 (because you skip the previous house), OR
            # 2. Skip the current house and keep the value from prev1
            curr = max(nums[i] + prev2, prev1)
            
            # Step 5: Move the window forward: prev2 becomes prev1, prev1 becomes curr
            prev2 = prev1
            prev1 = curr

        # Step 6: prev1 now contains the maximum amount we can rob without alerting the police
        return prev1