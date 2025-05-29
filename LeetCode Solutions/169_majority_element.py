class Solution:
    def majorityElement(self, nums):
############# Solution 1 Run-time: 19ms, Mem: 13.76 Mb #####################
        my_dictionary = {}
        for i in nums:
            if i not in my_dictionary.keys():
              my_dictionary[i] = 1
            else:
              my_dictionary[i] =  my_dictionary[i] + 1

            if my_dictionary[i] > len(nums)/2:
                return i

############# Solution 2 (Bad solution) #####################
        # count , max_val = 0,0
        # for index, value in enumerate(nums):
        #    if value == max_val:
        #        continue
        #    if nums.count(value) > count:
        #        count =  nums.count(value)
        #        max_val = value
        #
        # return max_val


############# Solution 2 (Best solution by others) #####################

        # nums.sort()
        # # print(nums)
        # # print(len(nums) // 2)
        # return nums[len(nums) // 2]

nums=[2, 2, 1, 1,3,3,3,3,3,3,3,3, 1, 2, 2]
arr = Solution()
print(arr.majorityElement(nums))