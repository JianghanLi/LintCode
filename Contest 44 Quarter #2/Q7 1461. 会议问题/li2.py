import bisect

# coding=utf-8
# Author: lee215
# Problem: 1066.Rectangle-Area-II
# Complexity: O(NlogN)
# Date: 2018-05-30

class Node(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.leaf = True

class ST(object):

    def __init__(self, a, b):
        self.root = Node(a, b)

    def pause(self, r1, r2):
        def jiao(o1, o2, r1, r2):
            return max(o1, r1) <= min(o2, r2)
        def update(root):
            if not root: return
            o1, o2 = root.start, root.end
            if not jiao(o1, o2, r1, r2): return
            if r1 <= o1 <= o2 <= r2:
                return -1
            if root.leaf == False:
                if root.left:
                    o1, o2 = root.left.start, root.left.end
                    if jiao(o1, o2, r1, r2):
                        if update(root.left) == -1:
                            root.left = None
                if root.right:
                    o1, o2 = root.right.start, root.right.end
                    if jiao(o1, o2, r1, r2):
                        if update(root.right) == -1:
                            root.right = None
                return
            o1, o2 = root.start, root.end
            if o1 < r1 <= o2 <= r2:
                root.start, root.end = [o1, r1 - 1]
            elif r1 <= o1 <= r2 < o2:
                root.start, root.end = [r2 + 1, o2]
            elif r1 <= o1 <= o2 <= r2:
                print "Oops again"
            elif o1 < r1 <= r2 < o2:
                root.leaf = False
                root.left = Node(o1, r1 - 1)
                root.right = Node(r2 + 1, o2)
            else:
                print "Oops", o1, o2, r1, r2
        if update(self.root) == -1:
            self.root = None

    def query(self, q):
        def que(root):
            if not root: return False
            if root.leaf:
                return root.start <= q <= root.end
            if root.left:
                if root.left.start <= q <= root.left.end:
                    return que(root.left)
            if root.right:
                if root.right.start <= q <= root.right.end:
                    return que(root.right)
            return False
        return que(self.root)

    def ptree(self):
        def p(root):
            if not root: return
            if root.left: p(root.left)
            if root.right: p(root.right)
            if root.leaf:
                print[root.start, root.end],
        p(self.root)

    def get_inter(self):
        self.inters = []
        def p(root):
            if not root: return
            if root.left: p(root.left)
            if root.right: p(root.right)
            if root.leaf:
                self.inters.append([root.start, root.end])
        p(self.root)
        return self.inters


class Solution:
    """
    @param meeting: The meetings
    @param pause: The pause time of meetings
    @param query: The query
    @return: Return the answer of each query
    """
    def getQuery(self, meeting, pause, query):
        mee = {}
        for i, a, b in meeting:
            mee[i] = ST(a, b)
        for i, r1, r2 in pause:
            mee[i].pause(r1, r2)

        inters = []
        for i in mee:
            inters.extend(mee[i].get_inter())
        count = []
        for a, b in inters:
            count.append([a, 1])
            count.append([b + 1, -1])
        count.sort()
        res = {}
        cur = 0
        for t, v in count:
            cur += v
            res[t] = cur

            # for i in range(len(expected)):
            #     if res[i] != expected[i]:
            #         print "wrong here", i, query[i], res[i], expected[i]
        res2 = []
        res_key = sorted(res.keys())
        # print res
        # print res_key
        for q in query:
            i = bisect.bisect_right(res_key, q) - 1
            # print q, i
            if i < 0:
                res2.append(0)
            else:
                res2.append(res[res_key[i]])
        return res2


############ test cases ###########
s = Solution()
# print s.getQuery(meeting=[[1, 1, 10]], pause=[[1, 1, 2], [1, 1, 4], [1, 9, 10], [1, 6, 7]], query=[1, 5, 8, 10])  # [0, 1, 1, 0]
# print s.getQuery(meeting=[[1, 1, 5], [2, 2, 8], [3, 1, 4]], pause=[[1, 1, 2], [1, 1, 4], [2, 5, 6], [2, 7, 7]], query=[1, 2, 3, 4, 5])  # [1, 2, 2, 2, 1]
# print s.getQuery([[3, 9, 12], [6, 8, 12], [9, 6, 8], [12, 7, 11]],
#                  [[3, 12, 12], [6, 12, 12], [6, 12, 12], [9, 8, 8], [3, 12, 12], [6, 11, 12], [6, 9, 11]],
#                  [0, 3, 6])  # [0, 0, 1]
# print s.getQuery([[3, 10, 11], [6, 4, 10], [9, 1, 10], [12, 10, 10], [15, 3, 5], [18, 8, 10], [21, 8, 8], [24, 8, 13]],
#                  [[21, 8, 8], [24, 13, 13], [18, 9, 10], [21, 8, 8], [3, 11, 11], [15, 5, 5], [3, 11, 11]],
#                  [6, 8, 9, 1, 4, 3, 8, 7])  # [2, 4, 3, 1, 3, 2, 4, 2]


f = open("7.in")
meeting = eval(f.readline())
pause = eval(f.readline())
query = eval(f.readline())

f2 = open("7.out")
expected = eval(f2.readline())

s.getQuery(meeting, pause, query)
