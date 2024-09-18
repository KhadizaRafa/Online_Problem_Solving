class Solution:
    def isValid(self, s: str) -> bool:
        p ={
            '(':')',
            '{':'}',
            '[':']'
        }
        q = []
        for i in s:
            if i in p.keys():
                q.append(i)
            else:
                m = q.pop()
                if i != p.get(m):
                    return False
        return False if len(q) else True


strs = "["
arr=Solution()
print(arr.isValid(strs))



