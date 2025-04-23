class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        tdict = {}

        if  len_s==0 or len_t==0 or len_s != len_t:
            return False
        else:
            for i in range(len(s)):
                if tdict.get(t[i])
                tdict[s[i]]=t[i]


        print(tdict)
        return False




res = Solution()
print(res.isIsomorphic('adg','egg'))