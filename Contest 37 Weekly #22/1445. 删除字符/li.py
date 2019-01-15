class Solution:
    """
    @param s: The string s
    @param t: The string t
    @return: Return if can get the string t
    """
    def canGetString(self, s, t):
        # Write your code here
        it = iter(s)
        try:
            for i in t:
                while i != next(it):
                    pass
            return True
        except:
            return False

############ test cases ###########
s = Solution()
print s.canGetString(s="abc", t="c")
print s.canGetString(s="a", t="c")


# https://www.lintcode.com/problem/delete-characters/description
