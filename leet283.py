def moveZeroes(nums):
    temp = 0
    for i in range(0, len(nums)):
        temp = nums[i]
        if nums[i] == 0: 
            nums.remove(nums[i])
            nums.append(temp)