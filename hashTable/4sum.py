def fourSum(nums, target):
    dicPair = {}
    result = []

    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            dicPair[nums[i] + nums[j]] = [i, j];

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                remainSum = nums[i] + nums[j]
                if (target - remainSum) in dicPair:
                    pair = dicPair[target - remainSum]
                    if pair[0] != i and pair[0] != j and pair[1] != i and pair[1] != j:
                        newSum = sorted([nums[i], nums[j], nums[pair[0]], nums[pair[1]]])
                        if newSum not in result:
                            result.append(newSum)

    return result


nums = [1, 0, -1, 0, -2, 2]
target = 0
#print(fourSum(nums, target))


# Mai Mai testing 2
#Mai Mai testing 2
