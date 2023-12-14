class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [0]*n

        # answer[i] contains the product of all the numbers to the left of i
        answer[0] = 1
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]
        # r_product contains the product of all the numbers to the right of i
        r_product = 1
        for i in reversed(range(n)):

        # For the index 'i', r_product would contain the product of all numbers to the right. We update r_product accordingly
            answer[i] = answer[i] * r_product
            r_product *= nums[i]

        print(answer)


res = Solution()
res.productExceptSelf([1, 2, 3, 4])
res.productExceptSelf([-1,1,0,-3,3])
