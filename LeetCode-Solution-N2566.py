# LeetCode Problem N2566: Minimum Difference by Changing One Digit
# Difficulty: Easy

class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        # Step 1: Convert the number to a string to manipulate its digits
        nums = str(num)
        
        # Step 2: Initialize variables to hold the maximum and minimum values
        big = str(num)
        small = str(num)
        
        # Step 3: Initialize a variable to track the first digit that is not '9' (it will be remapped for maximum)
        digit_for_big = ""
        
        # Step 4: Iterate through the digits of the number
        for i in range(len(nums)):
            
            # If the current digit is not '9', we can change it to '9' for maximum
            if digit_for_big == "" and nums[i] != "9":
                digit_for_big = nums[i]
            
            # If the current digit is equal to the digit we want to change for maximum, we change it to '9'
            if nums[i] == digit_for_big and digit_for_big != "":
                big = big[:i] + "9" + big[i+1:]

            # If the current digit is equal to the first digit, we can change it to '0' for minimum
            if nums[i] == nums[0]:
                small = small[:i] + "0" + small[i+1:]
                
        # Step 5: Return the difference between the maximum and minimum values
        return (int(big) - int(small))
    
num = 11891
num1 = 90
solution = Solution()
print(solution.minMaxDifference(num))  # Output: 99009
print(solution.minMaxDifference(num1))  # Output: 90