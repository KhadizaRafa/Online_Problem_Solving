class Solution(object):
    def threeSum(self, nums,target):
        nums.sort()
        diff= []
        print(nums)
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while(left<right):
                print(nums[i] , nums[left], nums[right])
                diff.append(target - (nums[i]+nums[left]+ nums[right]))
                if sum < target:
                    left = left + 1
                elif sum > target:
                    right = right - 1


                print(diff)
                left = left + 1
                right = right - 1


arr=Solution()
print(arr.threeSum( [-1,2,1,-4],1))