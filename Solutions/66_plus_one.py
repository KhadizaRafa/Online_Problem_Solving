class Solution:



    def plusOne(self, digits: [int]) -> [int]:
        list_len = len(digits)

        while(list_len):
            list_len-=1
            # print(list_len,digits[list_len])
            value = digits[list_len]+1
            if value%10==0 and value/10==1:
                digits[list_len] = 0
                if list_len==0:
                    digits.insert(0, 1)
            else:
                digits[list_len] += 1
                break

        return digits


nums=[9]
arr=Solution()
print(arr.plusOne(nums))