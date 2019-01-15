class Solution:
    """
    @param s: the string
    @param k: the max time to remove characters
    @return: Please output the new string with the smallest lexicographic order.
    """
    def MinimumString(self, s, k):
        # Write your code here
        stack = []
        remove = 0
        for c in s:
            while stack and stack[-1] > c and remove < k:
                stack.pop()
                remove += 1
            stack.append(c)
        while remove < k:
            stack.pop()
            remove += 1

        return "".join(stack)

############ test cases ###########
s = Solution()
print s.MinimumString(s="abccc", k=2)
print s.MinimumString(s="bacdb", k=2)
