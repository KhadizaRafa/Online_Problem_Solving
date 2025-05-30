import re
class Solution(object):
    def isPalindrome(self, s):
########## Solution 1 ##################
        # new_str = ''
        # for i in s:
        #     val = ord(i.lower())
        #     if (val>=48 and val<=57) or (val >= 97 and val <= 122):
        #         new_str+=i.lower()
        #
        # return new_str == new_str[::-1]


########## Solution 2 ##################
        pattern = "".join(re.findall(r'\b[0-9a-z]+\b',s.lower()))
        return pattern == pattern[::-1]

arr=Solution()
print(arr.isPalindrome("A man, a plan, a canal: Panama"))