# LeetCode problem N3201: Maximum Length of Alternating Parity Subsequence I
# Difficulty: Medium

from typing import List

class Solution:
    
    # Brute force solution: O(n^2)
    def maximumLength(self, nums: List[int]) -> int:
        
       # Step 1: Get the size of the array
        n = len(nums)
        res = 0

        # Step 2: Try both parities — looking for longest subsequence with either:
        #         a) Even adjacent sums (target_parity = 0), or
        #         b) Odd adjacent sums (target_parity = 1)
        for target_parity in [0, 1]:
            max_len = 1  # Minimum subsequence length is 1

            # Step 3: Try starting from each index
            for i in range(n):
                cnt = 1          # Start a new subsequence
                prev = nums[i]   # The last number added to the sequence

                # Step 4: Try building a sequence from nums[i]
                for j in range(i + 1, n):
                    # If the sum of previous + current matches target parity (even/odd)
                    if (prev + nums[j]) % 2 == target_parity:
                        cnt += 1
                        prev = nums[j]  # Update previous number
                # Step 5: Update max_len for current parity
                max_len = max(max_len, cnt)

            # Step 6: Update the final result across both parities
            res = max(res, max_len)

        # Step 7: Return the longest valid subsequence length found
        return res

    def maximumLengthOptimized(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Initialize parity counters for odd/even only sequences
        odd_count = 1 if nums[0] % 2 == 1 else 0
        even_count = 1 if nums[0] % 2 == 0 else 0

        # Step 2: Start an alternating sequence
        alternate_count = 1
        expecting_even = True if nums[0] % 2 == 1 else False  # Based on first number

        for i in range(1, n):
            # Step 3: If current number matches the expected parity, continue alternate sequence
            if (expecting_even and nums[i] % 2 == 0) or (not expecting_even and nums[i] % 2 == 1):
                alternate_count += 1
                expecting_even = not expecting_even  # Flip expectation

            # Step 4: Update odd/even counters
            if nums[i] % 2 == 1:
                odd_count += 1
            else:
                even_count += 1

        # Step 5: Return the longest count among odd-only, even-only, or alternating
        return max(even_count, odd_count, alternate_count)

    def maximumLengthBest(self, nums: List[int]) -> int:
        # Step 1: Initialize 4 counters to track:
        #   a) Longest odd-only subsequence (odd_prev_p)
        #   b) Longest alternating ending in odd after even (odd_prev_q)
        #   c) Longest even-only subsequence (even_prev_p)
        #   d) Longest alternating ending in even after odd (even_prev_q)
        odd_prev_p = 0
        odd_prev_q = 0
        even_prev_p = 0
        even_prev_q = 0

        # Step 2: Iterate over each number
        for num in nums:
            if num % 2 == 1:
                # If number is odd:
                odd_prev_p += 1                    # Extend odd-only count
                odd_prev_q = 1 + even_prev_q       # Extend alternating: even → odd
            else:
                # If number is even:
                even_prev_p += 1                   # Extend even-only count
                even_prev_q = 1 + odd_prev_q       # Extend alternating: odd → even

        # Step 3: Return the max among all 4 subsequences
        return max(odd_prev_p, odd_prev_q, even_prev_p, even_prev_q)
    
nums = [1,2,3,4]
nums1 = [1,2,1,1,2,1,2]
nums2 = [1,3]
sol = Solution()
print(sol.maximumLength(nums))          # Output: 4
print(sol.maximumLengthOptimized(nums1))  # Output: 7
print(sol.maximumLengthBest(nums2))     # Output: 2