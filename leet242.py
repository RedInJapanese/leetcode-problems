class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        d = []
        for i in s: 
            d.append(i)
        for i in t: 
            if i not in d:
                return False
            else:
                d.remove(i)
        return True