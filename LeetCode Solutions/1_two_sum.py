class Solution(object):
    ################ Solution 1 ############
    # def twoSum(self, nums, target):
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

    ################ Solution 2 ################# (better performance)
    def twoSum(self, nums, target):
        for index,num in enumerate(nums):
            sub = target - num
            if sub in nums and index!= nums.index(sub):
                    return [index, nums.index(sub)]


nums = [3,3]
target = 6
res = Solution()
print(res.twoSum(nums,target))