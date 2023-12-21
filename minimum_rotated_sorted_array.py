class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        This function performs a binary search on the input list nums.
        The idea is to find the "inflection point" in the list, which is the smallest number.
        This point can be found by comparing the middle element of the search space with its neighbours.
        If the middle element is greater than the next one, then the next one is the smallest.
        If the middle element is less than the previous one, then it is the smallest.
        If neither condition is met, then the inflection point is in the second half of the search
        space if the middle element is greater than the first element of nums, and in the first half otherwise.
        The function then continues to search in the appropriate half until it finds the inflection point. (edited)
        """
        # return sorted(nums)
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


sol = Solution()
print(sol.findMin([2, 9, 7, 5, 1]))