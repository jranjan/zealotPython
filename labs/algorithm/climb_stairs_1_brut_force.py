# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
# Approach: Brute Force
#
# Time complexity : O(2^n)
# Size of recursion tree will be 2^n
#
# The complexity was visible when we were running the code for 34 steps and more.
# The algorithm worked perfectly fine till that steps. This is why Google and
# other companies are specific about time and space complexity.
#
# It is not only important to write correct code but good code as well!
# Think like a birary tree and taking two setps. So, the complexity is
# sum of nodes at each level:
#
# 1 -> 2 > 2^2 -> 2^3 -> 2^4 ... 2^n


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._climb_stairs(0, n)

    def _climb_stairs(self, i, n):
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

        return self._climb_stairs(i + 1, n) + self._climb_stairs(i + 2, n)
