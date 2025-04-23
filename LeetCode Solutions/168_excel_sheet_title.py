class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        title = ''
        remainder = columnNumber%26
        columnNumber = columnNumber // 26
        if remainder!=0:
            title = chr(remainder+64) +title
        if columnNumber != 0:
            title = chr(columnNumber+64) +title
        return title

num = 52
res = Solution()
print(res.convertToTitle(num))