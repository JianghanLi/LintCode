class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitchWords(self, S):
        # Write your code here
        i, j, N = 0, 0, len(S)
        res = []
        while j < N:
            while j < N and S[j] == S[i]:
                j += 1
            if j - i >= 3:
                res.append((i, j - 1))
            i = j
        return res
