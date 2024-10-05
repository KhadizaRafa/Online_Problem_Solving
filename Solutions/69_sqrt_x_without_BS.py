class Solution(object):
    def mySqrt(self, x):
        i = 0
        mul = i*i
        while(mul < x):
            mul = i * i
            if mul>x:
                return i-1
            elif mul < x:
                i += 1
            else:
                return i
        return i

res = Solution()
print(res.mySqrt(0))