class Solution(object):

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

########## My Solution #######################
    # def romanToInt(self, s):
    #     roman = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        # sum = roman.get(s[0])
        # for i in range(1,len(s)):
        #     sum = sum + roman.get(s[i])
        #     if (s[i]== "V" or s[i]=='X') and s[i-1]=='I':
        #         sum = sum - 2
        #     if (s[i]== "L" or s[i]=='C') and s[i-1]=='X':
        #         sum = sum - 20
        #     if (s[i]== "D" or s[i]=='M') and s[i-1]=='C':
        #         sum = sum - 200
        # return sum

########## A Better Solution #######################
   def romanToInt(self, s):
        roman = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman.get(char)
            if value < prev_value:
                 total -= value  # Subtract if a smaller numeral comes before a larger one
            else:
                 total += value

            prev_value = value

        return total

res = Solution()
print(res.romanToInt('XXIX'))