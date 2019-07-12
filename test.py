class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs(0, n)

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
    