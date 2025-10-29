class Solution(object):

    def removeDuplicates(self, nums):
        # shouldn't use pop in a loop
        # for i in range(len(nums) - 1, 0, -1):
        #     if nums[i] == nums[i - 1]:
        #         nums.pop(i)
        #
        # return len(nums)
        i = 1
        j = 1

        while(j!= len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

nums = [0,0,1,1,1,2,2,3,3,4]
res = Solution()
print(res.removeDuplicates(nums))

# [0,1,2,2,3,3,4]
# res.test(nums,m,[2,2],val)