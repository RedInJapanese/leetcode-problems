def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hash = {}
    j = 0
    for i in nums: 
        if i in hash and j!=hash[i]:
            return True
        else:
            hash[i] = j
        j+=1
    return False