import enum


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lol = []
        d = {} 
        k = 0
        f = 0
        for i in nums:
            d[i]=f
            f+=1
        for x in nums: 
            if target-x in d:
                if(k != d[target-x]):
                    lol.append(k)
                    lol.append(d[target-x])
                    return lol
            k+=1
nums = [-3,4,3,90]
output = twoSum(nums, 0)
print(output)