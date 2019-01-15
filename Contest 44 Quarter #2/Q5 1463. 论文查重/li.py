# coding=utf-8
# Author: lee215
class Solution:
    """
    @param words1: the words in paper1
    @param words2: the words in paper2
    @param pairs: the similar words pair
    @return: the similarity of the two papers
    """
    def getSimilarity(self, words1, words2, pairs):
        for a, b in pairs:
            if a == "wtkqkayfiw" or b == "wtkqkayfiw":
                print a, b

        parents = {}
        self.count = 0
        def add(x):
            if x not in parents:
                parents[x] = x
                self.count += 1
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1
                return True
            return False

        for a, b in pairs:
            add(a)
            add(b)
            union(a, b)
        # print parents
        # print self.count
        words = set(words1 + words2 + [w[0] for w in pairs] + [w[1] for w in pairs])
        w2i = {}
        c = 0

        for w in words:
            if w in parents:
                w = find(w)
            # if w != 'gqbrjgfqsa':
            #     print w
            if w not in w2i:
                w2i[w] = c
                c += 1

        def w2if(w):
            if w in parents: w = find(w)
            return w2i[w]
        w1 = [w2if(w) for w in words1]
        w2 = [w2if(w) for w in words2]

        m, n = len(words1), len(words2)
        res = 0

        def find_lcseque(s1, s2):
             # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
            m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
            # d用来记录转移方向
            d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

            for p1 in range(len(s1)):
                for p2 in range(len(s2)):
                    if s1[p1] == s2[p2]:  # 字符匹配成功，则该位置的值为左上方的值加1
                        m[p1 + 1][p2 + 1] = m[p1][p2] + 1
                        d[p1 + 1][p2 + 1] = 'ok'
                    elif m[p1 + 1][p2] > m[p1][p2 + 1]:  # 左值大于上值，则该位置的值为左值，并标记回溯时的方向
                        m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
                        d[p1 + 1][p2 + 1] = 'left'
                    else:  # 上值大于左值，则该位置的值为上值，并标记方向up
                        m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
                        d[p1 + 1][p2 + 1] = 'up'
            (p1, p2) = (len(s1), len(s2))
            # print numpy.array(d)
            s = []
            while m[p1][p2]:  # 不为None时
                c = d[p1][p2]
                if c == 'ok':  # 匹配成功，插入该字符，并向左上角找下一个
                    s.append(s1[p1 - 1])
                    p1 -= 1
                    p2 -= 1
                if c == 'left':  # 根据标记，向左找下一个
                    p2 -= 1
                if c == 'up':  # 根据标记，向上找下一个
                    p1 -= 1
            s.reverse()
            return s

        common = find_lcseque(w1, w2)
        # print res, m, n
        return len(common) * 2 / float(m + n)


############ test cases ###########
s = Solution()
# print s.getSimilarity(words1=["great", "acting", "skills", "life"], words2=["fine", "drama", "talent", "health"], pairs=[["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]])
# print s.getSimilarity(words1=["I", "love", "you"], words2=["you", "love", "me"], pairs=[["I", "me"]])

f = open("3.in")
words1 = eval(f.readline())
words2 = eval(f.readline())
pairs = eval(f.readline())

print s.getSimilarity(words1, words2, pairs)
