import enum


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        weeder = []
        lol = []
        d = {} 
        x = 1
        k = 0
        j = 0
        f = 0
        while(k<len(nums)):
            while(x<len(nums)):
                if(nums[x] == target-nums[k]):
                    lol.append(k)
                    lol.append(x)
                    return lol
                x+=1
            k+=1
            x = k+1
nums = [-3,4,3,90]
output = twoSum(nums, 0)
print(output)