class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        for i in range(1,len(nums)):
            nums[i]+= nums[i-1]

        return nums


nums=[1,2,3,4]
arr=Solution()
print(arr.runningSum(nums))