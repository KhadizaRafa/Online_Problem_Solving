class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        max = -999
        for account in accounts:
            sum = 0
            for i in account:
                sum = sum+i

            if sum > max:
                max = sum

        return max


nums=[[1,5],[7,3],[3,5]]
arr=Solution()
print(arr.maximumWealth(nums))