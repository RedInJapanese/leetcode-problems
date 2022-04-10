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
        for i in nums: 
            if(i<=target):
                d[f] = j
                weeder.append(i)
                f+=1
            j+=1
        while(k<len(weeder)):
            while(x<len(weeder)):
                if(weeder[x] == target - weeder[k]):
                    lol.append(d[k])
                    lol.append(d[x])
                    return lol
                x+=1
            k+=1
            x = k+1
nums = [22,0,11,9]
output = twoSum(nums, 9)
print(output)