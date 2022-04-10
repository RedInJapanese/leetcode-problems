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
        check = 0
        for i in nums: 
            if(i<=target):
                d[i] = j
                weeder.append(i)
            j+=1
        while(k<len(weeder)):
            while(x<len(weeder)):
                if(weeder[x] == target - weeder[k]):
                    lol.append(d[weeder[k]])
                    lol.append(d[weeder[x]])
                    return lol
                x+=1
            k+=1
            x = k+1
nums = [22,0,11,9]
output = twoSum(nums, 9)
print(output)