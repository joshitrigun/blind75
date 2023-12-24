class Solution:
    def search(self, nums, target):
        """
        In this function, the low and high variables represent the start and end indices of the array.
        The mid variable is the middle index of the current search space. If the target is equal to the element
        at the middle index, the function returns the middle index. If the target is not found in the current
        search space, the function narrows down the search space to the half where the target could be present.
        The time complexity of this algorithm is O(log n), where n is the number of elements in the array. (edited)


        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
    # def search(self, nums: List[int], target: int) -> int:
    #     def find_rotate_index(left, right):
    #         if nums[left] < nums[right]:
    #             return 0
    #
    #         while left <= right:
    #             pivot = (left + right) // 2
    #             if nums[pivot] > nums[pivot + 1]:
    #                 return pivot + 1
    #             else:
    #                 if nums[pivot] < nums[left]:
    #                     right = pivot - 1
    #                 else:
    #                     left = pivot + 1
    #
    #     def binary_search(left, right):
    #         while left <= right:
    #             pivot = (left + right) // 2
    #             if nums[pivot] == target:
    #                 return pivot
    #             else:
    #                 if target < nums[pivot]:
    #                     right = pivot - 1
    #                 else:
    #                     left = pivot + 1
    #         return -1
    #
    #     n = len(nums)
    #
    #     if n == 1:
    #         return 0 if nums[0] == target else -1
    #
    #     rotate_index = find_rotate_index(0, n - 1)
    #
    #     if nums[rotate_index] == target:
    #         return rotate_index
    #     if rotate_index == 0:
    #         return binary_search(0, n - 1)
    #     if target < nums[0]:
    #         return binary_search(rotate_index, n - 1)
    #     return binary_search(0, rotate_index)
