class Solution(object):
    def romanToInt(self, s):
        roman = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        val = 0
        for i in range (len(s)):
            if i+1!=len(s) and ((s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')) or
                (s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C')) or
                (s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'))):
                val -= roman.get(s[i])
            else:
                val += roman.get(s[i])
        return val

res = Solution()
print(res.romanToInt('IV'))