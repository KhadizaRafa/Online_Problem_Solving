class Solution(object):
    def threeSum(self, nums):
        new_nums = sorted(nums)
        res = []
        # print(new_nums)

        for i in range(len(new_nums)-2):
            # Skip duplicates for i
            if i > 0 and new_nums[i] == new_nums[i - 1]:
                continue

            low = i+1
            high=len(nums) - 1
            while(low<high):
                # print(new_nums[i],new_nums[low], new_nums[high])
                sum = new_nums[high]+new_nums[low]+ new_nums[i]
                # print("sum:"+str(sum))
                if sum < 0:
                    low = low+1
                elif sum>0:
                    high = high-1
                else:
                    res.append([new_nums[i],new_nums[low], new_nums[high]])
                    # Skip duplicates for left
                    while low < high and new_nums[low] == new_nums[low + 1]:
                        low+=1
                    # Skip duplicates for right
                    while low < high and new_nums[high] == new_nums[high - 1]:
                        high-=1

                    low+=1
                    high-=1


        return res

arr=Solution()
print(arr.threeSum([-1,0,1,2,-1,-4]))