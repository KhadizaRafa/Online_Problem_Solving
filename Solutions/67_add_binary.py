class Solution:
    def addBinary(self, a: str, b: str) -> str:
        k = len(a) if len(a)>len(b) else len(b)
        carry = 0
        res=''
        while k:
           r = int(a[k-1]) +int(b[k-1])+carry
           if r>1:
               carry = 1
               res+='0'
           else:
               res+=str(r)
        #
        # i = len(a)-len(b)
        # if i<0:
        #     a = '0' * abs(i) + a
        # else:
        #     b='0'* i + b
        #
        # a = a[::-1]
        # b = b[::-1]
        #
        # for j in range(len(a)):
        #   if int(a[j])+int(b[j])+carry > 1:
        #       carry = 1

        return res


a = "1100"
b = "100"
arr=Solution()
print(arr.addBinary(a,b))