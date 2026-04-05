class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1

        profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                if current_profit > profit:
                    profit = current_profit
            else:
                left = right
            right += 1
        
        return profit