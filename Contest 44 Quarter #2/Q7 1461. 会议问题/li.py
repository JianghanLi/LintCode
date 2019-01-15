import bisect
class Solution:
    """
    @param meeting: The meetings
    @param pause: The pause time of meetings
    @param query: The query
    @return: Return the answer of each query
    """
    def getQuery(self, meeting, pause, query):
        inf = float('inf')
        # Write your code here
        def jiao(o1, o2, r1, r2):
            return max(o1, r1) <= min(o2, r2)
        mee = {}
        for i, a, b in meeting:
            mee[i] = [[a, b]]
        for i, r1, r2 in pause:
            inters = mee[i]
            j1 = bisect.bisect(inters, [r1, -inf])
            j2 = bisect.bisect(inters, [r2, -inf])
            inters[j1 + 1:j2] = []
            for j in [j1, j1 + 1, j1 + 2]:
                if j >= len(inters): break
                o1, o2 = inters[j]
                if o2 < r1:
                    break
                if jiao(o1, o2, r1, r2):
                    if o1 < r1 <= o2 <= r2:
                        inters[j] = [o1, r1 - 1]
                    elif r1 <= o1 <= r2 < o2:
                        inters[j] = [r2 + 1, o2]
                    elif r1 <= o1 <= o2 <= r2:
                        inters[j:j + 1] = []
                    elif o1 < r1 <= r2 < o2:
                        inters[j:j + 1] = [[o1, r1 - 1], [r2 + 1, o2]]
                    else:
                        print "Oops", o1, o2, r1, r2
                j += 1
        # print mee
        def que(q):
            res = 0
            for i in mee:
                m = mee[i]
                j = bisect.bisect(m, [q, inf])
                if j == 0: continue
                if m[j - 1][0] <= q <= m[j - 1][1]: res += 1
            return res
        return [que(q) for q in query]

############ test cases ###########
s = Solution()
# print s.getQuery(meeting=[[1, 1, 10]], pause=[[1, 1, 2], [1, 1, 4], [1, 9, 10], [1, 6, 7]], query=[1, 5, 8, 10])
# print s.getQuery(meeting=[[1, 1, 5], [2, 2, 8], [3, 1, 4]], pause=[[1, 1, 2], [1, 1, 4], [2, 5, 6], [2, 7, 7]], query=[1, 2, 3, 4, 5])
# print s.getQuery([[3, 10, 11], [6, 4, 10], [9, 1, 10], [12, 10, 10], [15, 3, 5], [18, 8, 10], [21, 8, 8], [24, 8, 13]],
#                  [[21, 8, 8], [24, 13, 13], [18, 9, 10], [21, 8, 8], [3, 11, 11], [15, 5, 5], [3, 11, 11]],
#                  [6, 8, 9, 1, 4, 3, 8, 7])


f = open("4.in")
meeting = eval(f.readline())
pause = eval(f.readline())
query = eval(f.readline())

print s.getQuery(meeting, pause, query)
