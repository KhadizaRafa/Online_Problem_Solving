class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        reversed_num = 0

        while num!=0:
            if num < 0:
                return False
            remainder = num % 10
            reversed_num = reversed_num * 10 + remainder
            num = num // 10
        if reversed_num == x:
            return True
        return False


num=105
res = Solution()
print(res.isPalindrome(num))