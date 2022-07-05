def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {
            "1":1,
            "2":4,
            "3":9,
            "4":16,
            "5":25,
            "6":36,
            "7":49,
            "8":64,
            "9":81}
        c = {}
        sum = 0
        
        while n != 1:
            convert = str(n)
            sum = 0
            for i in convert:
                if i in d:
                    sum+=d[i]
            if sum not in c:
                c[sum] = 9
            else:
                break
            n = sum
        
        if(n==1):
            return True
        else:
            return False