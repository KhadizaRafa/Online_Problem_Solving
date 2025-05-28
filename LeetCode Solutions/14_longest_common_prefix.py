class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:

############# Solution 1 (Run time: 0 ms, Mem: 12.51 MB) ##########################
        shortest_str = strs[0]

        for str in strs:
            while not str.startswith(shortest_str):
                shortest_str = shortest_str[:-1]

        return shortest_str

############# Solution 2 (Run time: 7 ms, Mem: 12.53 MB)##########################

        i=0
        j=1
        shortest_str=strs[0]
        while j < len(strs):
            if i < len(strs[j]) and i < len(shortest_str) and shortest_str[i] == strs[j][i]:
                i=i + 1
            else:
                shortest_str=strs[j][0:i]
                j=j + 1
                i = 0

        return shortest_str



strs = ["dog","dracecar","dcar"]
arr=Solution()
print(arr.longestCommonPrefix(strs))