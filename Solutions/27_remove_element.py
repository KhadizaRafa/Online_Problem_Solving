class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=len(nums)
        while val in nums and i!=len(nums)-1:
             nums.remove(val)
             i=i+1
        return len(nums)


# Solution with 6ms runtime
        # i=0
        # for x in nums:
        #     if x != val:
        #         nums[i]=x
        #         i+=1
        # return i
        #


# My initial Solution
# class Solution(object):
#     def removeElement(self, nums, val):
#         i = 0
#         j = len(nums)-1
#         counter=0
#
#         if i==j and nums[i]==val:
#             return 0
#
#         while i<j:
#             if nums[i] == val:
#                 counter=counter + 1
#                 if nums[j] == val:
#                     j = j-1
#                     continue
#                 else:
#                     nums[i] = nums[j]
#                     nums[j] = val
#                     j = j - 1
#             i = i+1
#
#
#
#         return len(nums)-counter


nums = [3,2,2,3]
val = 3
res = Solution()
print(res.removeElement(nums,val))
# res.test(nums,m,[2,2],val)
