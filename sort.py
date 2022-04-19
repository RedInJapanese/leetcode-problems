def searchInsert(self, nums, target):
    x = 0    
    d = {}
    for i in nums:
        d[i] = x
        x+=1
    if target in d:
        return d[target]
    else:
        j = len(nums)
        while j>0 and target<nums[j-1]:
            j-=1
        return j