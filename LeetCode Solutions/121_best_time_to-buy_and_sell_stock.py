class Solution(object):
    # def maxProfit(self, prices):
    #     min_price = min(prices)
    #     min_day= prices.index(min_price)
    #     if min_day == len(prices) - 1:
    #         return 0
    #     p = prices[min_day+1:len(prices)]
    #     profit = max(p) - min_price
    #     if profit>0:
    #         return profit
    #     else:
    #         return 0

    def maxProfit(self, prices):
        p = [[index,value] for index, value in enumerate(prices)]

        print(sorted_p)
        return p
        # min_price = prices[0]
        # min_day = 0
        # p = prices
        # for index,price in enumerate(p):
        #     profit = price-min_price
        #     if profit<=min_price and index!=len(prices)-1:
        #         min_price = price
        #         p = p[index+1:len(prices)]
        #     elif profit<=min_price and index==len(prices)-1:
        #         p=p[index + 1:len(prices)]
        # return min_price


        # for index,price in enumerate(prices):
        #
        # min_price=min(prices)
        # min_day=prices.index(min_price)
        # if min_day == len(prices) - 1:
        #     return 0
        # p=prices[min_day + 1:len(prices)]
        # profit=max(p) - min_price
        # if profit > 0:
        #     return profit
        # else:
        #     return 0

res = Solution()
print(res.maxProfit([2,4,1]))