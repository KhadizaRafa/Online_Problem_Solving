class Solution(object):
    def merge(self, nums1, m, nums2, n):
        j = 0
        for index,value in enumerate(nums1):
            if value == 0 and j!=n:
                nums1[index] = nums2[j]
                j = j+1

        nums1.sort()





#
# nums1 = []
# m = 0
# nums2 = [1]
# n = 1
nums1=[1, 2, 3, 0, 0, 0]
m=3
nums2=[2, 5, 6]
n=3
res=Solution()
res.merge(nums1,m,nums2,n)
print(nums1)