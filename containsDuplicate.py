class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr1 = {}
        for i, num in enumerate(nums):
            if num in arr1:
                return True
            arr1[num] = i


duplicate = Solution()

duplicate.containsDuplicate([1, 2, 3, 4, 1])
duplicate.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

