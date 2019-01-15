# coding=utf-8
# 没有新题，怎么可以这么糊弄contest。
import itertools
class Solution:
    """
    @param target: the target string
    @param words: words array
    @return: whether the target can be matched or not
    """
    def matchFunction(self, target, words):
        # Write your code here
        possible = [[] for c in target]
        for i, c in enumerate(target):
            for j, w in enumerate(words):
                if c in w:
                    possible[i].append(j)
        s = set()
        def f(i):
            if i == len(target):
                return True
            for x in possible[i]:
                if x not in s:
                    s.add(x)
                    if f(i + 1): return True
                    s.remove(x)
            return False
        return f(0)

############ test cases ###########
s = Solution()
print s.matchFunction(target="ally", words=["buy", "discard", "lip", "yep"])
print s.matchFunction("abde", ["aa", "ab", "de", "de"])
print s.matchFunction("ntveejzatjmn", ["ctnmnyyzyd", "pbyqgoapszcw", "ydttoiwobbi", "oshxuypgw", "ajoznpdr", "dnszsadchwmmkuv", "orsnpqojnlwfmkvz", "hjxgqkfppmqpcea", "rhd", "ntpwfxlmw", "irlgbdev", "dbdrgqvqovpvwdmcpctd", "swxcfafyv"])
