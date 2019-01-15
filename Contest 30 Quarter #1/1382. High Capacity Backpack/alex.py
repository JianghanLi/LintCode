class Solution:
    """
    @param s: The capacity of backpack
    @param v: The value of goods
    @param c: The capacity of goods
    @return: The answer
    """
    def getMaxValue(self, cap, V, C):
        items = zip(V, C)
        N = len(V)

        def cleanup(D):
            ans = []
            p = 0
            for k in sorted(D):
                v = D[k]
                if v > p:
                    ans.append((k, v))
                    p = v
            return ans

        def solve(A):
            # A: (v, c)   value and cost
            M = len(A)
            points = {}
            for mask in xrange(1 << M):
                i = v = c = 0
                while mask:
                    if mask & 1:
                        v += A[i][0]
                        c += A[i][1]

                    mask >>= 1
                    i += 1
                points[c] = max(v, points.get(c, 0))
            return cleanup(points)

        points1 = [(0, 0)]
        points1.extend(solve(items[:N / 2]))
        points2 = [(0, 0)]
        points2.extend(solve(items[N / 2:]))

        # normal sum get TLE
        """
        ans = 0
        for c1, v1 in points1:
            for c2, v2 in points2:
                if c1 + c2 <= cap:
                    ans = max(ans, v1 + v2)
        return ans
        """

        # two pointers sum
        ans = 0
        i = 0
        j = len(points2) - 1
        while i < len(points1) and j >= 0:
            while j and points1[i][0] + points2[j][0] > cap:
                j -= 1
            if points1[i][0] + points2[j][0] <= cap:
                ans = max(ans, points1[i][1] + points2[j][1])
            i += 1
        return ans


############ comments ############
# 1 <= n <= 31
# 对每一半的物品暴力求组合
# 2 pointers 求2sum最大值
