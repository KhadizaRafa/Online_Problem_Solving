class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #   return -1


haystack = "sadbutsad"
needle = "buk"
arr=Solution()
print(arr.strStr(haystack,needle))