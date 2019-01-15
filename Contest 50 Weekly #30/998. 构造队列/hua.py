# 本参考程序来自九章算法，由 @华助教 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param n: The array sum
    @param arr1: The size
    @param arr2: How many numbers small than itself
    @return: The correct array
    """
    class SegmentTreeNode:

        def __init__(self, start, end):
            self.start, self.end = start, end
            self.left, self.right = None, None
            self.val = 0
    def build(self, l, r):
        if l > r:
            return None
        root = self.SegmentTreeNode(l, r)
        root.val = 1
        if l != r:
            mid = (l + r) / 2
            root.left = self.build(l, mid)
            root.right = self.build(mid + 1, r)
            root.val = root.left.val + root.right.val
        return root
    def query(self, x, root):
        if root.start == root.end:
            root.val = 0
            return root.start
        pos = 0
        if x <= root.left.val:
            pos = self.query(x, root.left)
        else:
            pos = self.query(x - root.left.val, root.right)
        root.val = root.left.val + root.right.val
        return pos
    def cmp(self, a, b):
        return b[0] - a[0]
    def getQueue(self, n, arr1, arr2):
        # Write your code here
        arr = [(arr1[i], arr2[i]) for i in range(n)]
        arr = sorted(arr, self.cmp)
        root = self.build(0, n - 1)
        ans = [0 for i in range(n)]
        for i in range(n):
            x = arr[i][0]
            y = arr[i][1]
            ans[self.query(y + 1, root)] = x
        return ans
