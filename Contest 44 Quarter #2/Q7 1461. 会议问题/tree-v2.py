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

    def pause(self, r1, r2, st2):
        def jiao(o1, o2, r1, r2):
            return max(o1, r1) <= min(o2, r2)
        def update(root):
            if not root: return
            o1, o2 = root.start, root.end
            if not jiao(o1, o2, r1, r2): return
            if r1 <= o1 <= o2 <= r2:
                st2.update(o1, o2, -1)
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
                st2.update(r1, o2, -1)
            elif r1 <= o1 <= r2 < o2:
                root.start, root.end = [r2 + 1, o2]
                st2.update(o1, r2, -1)
            elif r1 <= o1 <= o2 <= r2:
                print "Oops again"
            elif o1 < r1 <= r2 < o2:
                root.leaf = False
                root.left = Node(o1, r1 - 1)
                root.right = Node(r2 + 1, o2)
                st2.update(r1, r2, -1)
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


class Node2(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        self.left = None
        self.right = None

class ST2(object):

    def __init__(self, x):
        self.x_i = {v: i for i, v in enumerate(x)}
        self.x = x
        def createTree(l, r):
            if l > r: return None
            root = Node2(l, r)
            if l == r: return root
            mid = (l + r) / 2
            root.left = createTree(l, mid)
            root.right = createTree(mid + 1, r)
            return root
        self.root = createTree(0, len(x) - 1)

    def update(self, x1, x2, val):
        def updateVal(root, i, j):
            if root.start == i and root.end == j:
                root.count += val
            else:
                mid = (root.start + root.end) / 2
                if i <= mid:
                    updateVal(root.left, i, min(mid, j))
                if mid + 1 <= j:
                    updateVal(root.right, max(mid + 1, i), j)
        updateVal(self.root, self.x_i[x1], self.x_i[x2])

    def query(self, q):
        self.res = 0
        qi = bisect.bisect_left(self.x, q)
        if self.x[qi] > q:
            qi -= 1
        if qi < 0: return 0
        # print "query", int(qi), self.x[int(qi)], qi, q, int(qi + 1), self.x[int(qi + 1)]
        def que(root):
            if not root: return
            if root.start <= qi <= root.end:
                self.res += root.count
            if root.left:
                if root.left.start <= qi <= root.left.end:
                    que(root.left)
            if root.right:
                if root.right.start <= qi <= root.right.end:
                    que(root.right)
        que(self.root)
        return self.res

    def ptree(self):
        def p(root):
            if not root: return
            if root.left: p(root.left)
            if root.right: p(root.right)
            if root.count:
                print[root.start, root.end, root.count]
        p(self.root)

class Solution:
    """
    @param meeting: The meetings
    @param pause: The pause time of meetings
    @param query: The query
    @return: Return the answer of each query
    """
    def getQuery(self, meeting, pause, query):
        mee = {}
        x = set()
        for i, a, b in meeting:
            x.add(a + 1)
            x.add(a)
            x.add(a - 1)
            x.add(b)
            x.add(b - 1)
            x.add(b + 1)
        for i, r1, r2 in pause:
            x.add(r1)
            x.add(r1 + 1)
            x.add(r1 - 1)
            x.add(r2)
            x.add(r2 + 1)
            x.add(r2 - 1)
        x = sorted(x)
        st2 = ST2(x)
        for i, a, b in meeting:
            mee[i] = ST(a, b)
            st2.update(a, b, 1)
        for i, r1, r2 in pause:
            mee[i].pause(r1, r2, st2)

        # for i in mee:
        #     print i,
        #     mee[i].ptree()
        #     print
        # print
        # st2.ptree()

        # return [sum(mee[i].query(q) for i in mee) for q in query]
        res = [st2.query(q) for q in query]
        # expected = [18, 18, 30, 27, 18, 12, 10, 4, 13, 17, 22, 16, 12, 17, 28, 13, 13, 28, 4, 12, 16, 16, 29, 7, 13, 1, 14, 11, 3, 13, 3, 29, 17, 25, 13,
        #             28, 12, 16, 3, 1, 23, 3, 23, 13, 1, 13, 29, 13, 19, 5, 27, 3, 29, 12, 1, 13, 3, 30, 19, 11, 19, 1, 10, 14, 30, 28, 13, 31, 18, 1, 13, 20, 3]
        # for i in range(len(res)):
        #     if res[i] != expected[i]:
        #         print "wrong here", i, query[i], res[i], expected[i]
        # print st2.x
        return res
