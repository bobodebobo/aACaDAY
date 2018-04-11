class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [-1]*(amount+1)
        dp[0] = 0
        for i in range(0,amount+1):
            if dp[i] != -1:
                for j in coins:
                    if i+j > amount:
                        break
                    else:
                        if dp[i+j] != -1:
                            dp[i+j] = min(dp[i+j],dp[i]+1)
                        else:
                            dp[i+j] = dp[i]+1
        return dp[amount]
