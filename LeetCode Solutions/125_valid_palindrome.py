def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    low=1
    high=x
    # mid=(low + high) // 2
    while low < high:
        mid=(low + high) // 2
        res=mid * mid
        if res > x:
            high=mid - 1
        elif res < x:
            low=mid + 1
        else:
            return mid
    return high
