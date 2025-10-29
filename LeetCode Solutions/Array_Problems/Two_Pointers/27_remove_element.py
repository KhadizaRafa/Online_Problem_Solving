class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # shouldn't use remove in a loop
        # i=len(nums)
        # while val in nums and i!=len(nums)-1:
        #      nums.remove(val)
        #      i=i+1
        # return len(nums)
        j = 0
        for i in range (len(nums)):
            if nums[i]!= val:
                if i!=j:
                    nums[j]=nums[i]
                j = j+1
        return j

nums = [2]
val = 0
res = Solution()
print(res.removeElement(nums,val))
print(nums)

