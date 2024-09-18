class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:

        shortest_str = strs[0]

        for str in strs:
            while not str.startswith(shortest_str):
                shortest_str = shortest_str[:-1]

        return shortest_str


strs = ["flow","reflower","flight"]
arr=Solution()
print(arr.longestCommonPrefix(strs))