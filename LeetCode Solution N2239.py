class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        #Step 1: Make a variable to hold value while we iterate through the list
        answer = nums[0]

        #Step 2: Iterate through the list
        for num in nums:

            #Step 3: Set condition to get the value with the smallest absolute value
            if abs(num) < abs(answer):
                answer = num

            #Step 4: Set condition to get the positive value when their absolute one's are equal
            elif abs(answer) == abs(num) and answer < num:
                answer = num
                
        #Step 5: Return the answer
        return answer
    
nums1 = [-4,-2,1,4,8]
nums2 = [2,-1,1]
sol = Solution()
print(sol.findClosestNumber(nums1))  # Output: 1
print(sol.findClosestNumber(nums2))  # Output: 1