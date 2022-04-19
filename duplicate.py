def removeDuplicates(self, nums):
    d = {}
    x = 0
    for i in nums:
        if i in d:
            nums.remove(x)
        d[i] = x
        x+=1
    return nums