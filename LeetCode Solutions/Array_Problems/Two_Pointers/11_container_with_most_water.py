class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height) - 1
        max_area = 0

        while(low < high):
           area = min(height[high],height[low]) *  (high - low)
           max_area = max(max_area, area)

           if height[high]>height[low]:
               low+=1
           else:
               high-=1

        return max_area




result_obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(result_obj.maxArea(height))