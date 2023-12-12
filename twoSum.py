def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            print([num_map[target-num], i])
        num_map[num] = i

    return []


twoSum(nums=[2,7,11,15], target = 9)
twoSum(nums = [3,2,4], target = 6)