def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    buffer = str(x)
    if buffer == buffer[::-1]:
        return True
    return False

isPalindrome(121)