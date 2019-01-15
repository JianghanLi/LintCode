class Solution:
    """
    @param str: the string
    @return: the length of substring
    """
    def askingForTheLongest01Substring(self, str):
        # Write your code here
        str += str
        ans = 1
        cnt = 1
        for i in range(1, len(str)):
            if str[i] != str[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt and 2 * cnt <= len(str):
                ans = cnt
        return ans
