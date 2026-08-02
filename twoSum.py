def twoSum(nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashMap:
            return [hashMap[target - nums[i]], i]
        hashMap[nums[i]] = i


print(twoSum([1, 2, 3, 4, 5], 7))
