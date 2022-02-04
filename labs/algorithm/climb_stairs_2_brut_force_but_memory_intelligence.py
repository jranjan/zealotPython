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
        memo = [None] * n
        return self._climb_stairs(0, n, memo)

    def _climb_stairs(self, i, n, memo):
        # Every step, we are deciding how we can go above by 1 or 2 steps.
        # We are just adding up those numbers. Effectively, we are moving up
        # using recursion. At the same time, we need to terminal condition
        # and that will be as soon as we reach top and i.e. if current step
        # is the top most layer. Why not eeual? Because you have reached the
        # place where yo wanted to.


        if i > n:
            return 0

        if i == n:
            return 1

        if memo[i] > 0:
            return memo[i]

        return self._climb_stairs(i + 1, n, memo) + self._climb_stairs(i + 2,
                                                                       n, memo)