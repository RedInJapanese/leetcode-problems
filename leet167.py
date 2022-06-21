    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lol = []
        d = {} 
        k = 0
        f = 0
        for i in numbers:
            d[i]=f
            f+=1
        for x in numbers: 
            if target-x in d:
                if(k != d[target-x]):
                    lol.append(k+1)
                    lol.append((d[target-x])+1)
                    return lol
            k+=1