# See https://www.youtube.com/watch?v=vYquumk4nWw
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
# Approach: Recursion with Memoization
#
# But we are remembery the steps. So, we are leveraging memory!
# As a result, we do not need to go to each step too deep if we
# have calculated for a number. So, maxium is o(n).


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # Hey, we did not use recurzion here!
        # We saved memory by using nth array instead of going deep
        # in recursion with memory. So, we did not just save compute
        # time but we save space as well. Are you getting?
        for i in range(3, n + 1, 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
