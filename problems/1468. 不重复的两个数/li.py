class Solution:
    """
    @param a: the array
    @return: the two numbers that are not repeated
    """
    def theTwoNumbers(self, a):
        # Write your code here
        s = set()
        for i in a:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return sorted(s)
