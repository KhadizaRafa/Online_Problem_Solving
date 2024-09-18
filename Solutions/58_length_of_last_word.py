class Solution:
    def lengthOfLastWord(self, s) -> int:
        # l = s.strip().split(' ')
        # #you don't need to pass '' to split.If given l = ['', '', '', 'fly', 'me', '', '', 'to', '', '', 'the', 'moon', '', '']
        # if given only s.split() l = ['fly', 'me', 'to', 'the', 'moon']

        return len(s.split()[-1])

str = "   fly me   to   the moon  "
arr=Solution()
print(arr.lengthOfLastWord(str))

