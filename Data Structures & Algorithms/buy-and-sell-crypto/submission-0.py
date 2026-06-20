class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        left = 0
        right = n-1
        max_profit = 0
        for right in range(1, n):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right  # Found a cheaper buying day

        return max_profit