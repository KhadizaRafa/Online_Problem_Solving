class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range( i + 1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                low = j+1
                high = len(nums)-1
                while low < high:
                    sum=nums[i] + nums[j] + nums[low] + nums[high]
                    if sum < target:
                        low=low + 1
                    elif sum > target:
                        high=high - 1
                    else:
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        while low<high and nums[low] == nums[low + 1]:
                            low=low + 1
                        while low < high and nums[high] == nums[high - 1]:
                            high = high -1

                        low=low + 1
                        high=high - 1

        return result

nums = [1,1,2,2,2,2]
target = 6
res = Solution()
print(res.fourSum( nums,target))