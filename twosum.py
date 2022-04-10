def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        weeder = []
        lol = [] 
        x = 1
        k = 0
        j = 0
        for i in nums: 
            if(i>target):
                nums[j] = 0
            j+=1
        
        while(k<len(nums)):
            while(x<len(nums)):
                if(nums[x] == target - nums[k]):
                    lol.append(k)
                    lol.append(x)
                    return lol
                x+=1
            k+=1
            x = k+1
        #return weeder
nums = [2,7,11,15]
output = twoSum(nums, 9)
print(output)