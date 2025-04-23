class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # better Solution 1:
        # c=1
        # for i in range(len(nums) - 1):
        #     if nums[i] != nums[i + 1]:
        #         nums[c]=nums[i + 1]
        #         c+=1
        # return c

        # better Solution 2:
        # i=0
        # for j in range(1, len(arr)):
        #     if arr[i] != arr[j]:
        #         i+=1
        #         arr[i]=arr[j]
        # return i + 1


        # for i in range(len(nums)-1,0,-1):
        #     if nums[i] == nums[i-1]:
        #         nums.pop(i)
        #
        # return len(nums)


nums = [0,1,1,1,2,2,3,3,4]
res = Solution()
print(res.removeDuplicates(nums))
# res.test(nums,m,[2,2],val)