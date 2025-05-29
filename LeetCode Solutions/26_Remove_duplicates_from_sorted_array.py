class Solution(object):

    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)

        return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
res = Solution()
print(res.removeDuplicates(nums))
# res.test(nums,m,[2,2],val)