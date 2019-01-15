class Solution:
    """
    @param s: The string s
    @param excludeList: The excludeList
    @return: Return the most frequent words
    """
    def getWords(self, s, excludeList):
        ban = set(banned)
        words = re.sub(r'[^a-zA-Z]', ' ', p).lower().split()
        c = collections.Counter(w for w in words if w not in ban)
        big = max([c[i] for i in c] + [0])
        return [i for i in c if c[i] == big]
