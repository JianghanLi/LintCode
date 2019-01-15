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
        # for i in mee:
        #     mee[i].ptree()
        #     print
        return [sum(mee[i].query(q) for i in mee) for q in query]


############ test cases ###########
s = Solution()
print s.getQuery([[3, 10, 11], [6, 4, 10], [9, 1, 10], [12, 10, 10], [15, 3, 5], [18, 8, 10], [21, 8, 8], [24, 8, 13]],
                 [[21, 8, 8], [24, 13, 13], [18, 9, 10], [21, 8, 8], [3, 11, 11], [15, 5, 5], [3, 11, 11]],
                 [6, 8, 9, 1, 4, 3, 8, 7])
