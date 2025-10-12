class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0] * len(nums)
        low=0
        n=len(nums) - 1
        high=n

        while low <= high:
            if nums[low] ** 2 < nums[high] ** 2:
                res[n]=nums[high] ** 2
                high-=1
            else:
                res[n]=nums[low] ** 2
                low+=1
            n = n - 1
        return res


nums=[-4, -1, 0, 3, 10]
res=Solution()
res.sortedSquares(nums)
