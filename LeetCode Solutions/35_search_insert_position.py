class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if i >= target:
               return nums.index(i)

        return len(nums)

        # Better solution done using binary search
        #
        # low  = 0
        # high = len(nums)-1
        #
        # while high>low:
        #     mid = high+low//2
        #
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid]<target:
        #         low = mid + 1
        #     else:
        #         high = mid -1
        #
        # return low

nums = [1,2,4]
val = 8
res = Solution()
print(res.searchInsert(nums,val))
# res.test(nums,m,[2,2],val)