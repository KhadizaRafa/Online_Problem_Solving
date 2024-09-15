class Solution:
    def majorityElement(self, nums):
        my_dictionary = {}
        for i in nums:
            if i not in my_dictionary.keys():
              my_dictionary[i] = 1
            else:
              my_dictionary[i] =  my_dictionary[i] + 1

            if my_dictionary[i] > len(nums)/2:
                return i


nums=[2, 2, 1, 1, 1, 2, 2]
arr = Solution()
print(arr.majorityElement(nums))