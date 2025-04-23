class Solution:
    def isValid(self, s: str) -> bool:
        p ={
            '(':')',
            '{':'}',
            '[':']'
        }
        q= []

        if len(s)<2:
            return False
        for i in s:
            if i in p.keys():
                q.append(i)
            else:
                if len(q) and i == p.get(q.pop()):
                    continue
                else:
                    return False
        return False if len(q) else True


strs = "]]"
arr=Solution()
print(arr.isValid(strs))



