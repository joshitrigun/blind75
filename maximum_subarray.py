class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        
        curSum = maxSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        print(maxSum)


sol = Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

sol.maxSubArray([1])

sol.maxSubArray([5,4,-1,7,8])