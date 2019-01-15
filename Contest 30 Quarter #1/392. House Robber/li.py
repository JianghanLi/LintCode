class Solution(object):
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for n in nums:
            a, b = b, max(a + n, b)
        return b
