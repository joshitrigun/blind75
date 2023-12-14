class Solution:
    @staticmethod
    def maxProfit(prices):

        minPrice = float('inf')
        maxProfit = 0

        for price in prices:

            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        print(maxProfit)


m = Solution()
m.maxProfit([7, 1, 5, 3, 6, 4])
m.maxProfit([7, 6, 4, 3, 1])