class Solution:
    def addBinary(self, a: str, b: str) -> str:

        #### method 1 ######
        # a = int(a,2)
        # b = int(b,2)
        # return bin(a+b)[2:]
        # a = int(a,2)
        # print(a,b)


        #### method 2 ######
        m =''
        if len(a) < len(b):
            a = a.rjust(len(b), '0')

        else:
            b = b.rjust(len(a), '0')

        print(a,b)
        carry = 0
        res=0
        k=len(a)-1

        while k>-1:

            res = int(a[k]) + int(b[k])+ carry
            if res==2:
                carry=1
                m='0'+m
            elif res==3:
                carry=1
                m='1'+m
            else:
               m = str(res)+m
               carry=0
            k-=1
        return '1'+m if carry else m


a = "1111"
b = "1111"


# print(a.rjust(7, '0'))
arr=Solution()
print(arr.addBinary(a,b))