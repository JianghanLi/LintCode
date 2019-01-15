class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        parent = {}
        for s in sets:
            for i in s:
                parent[i] = i
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            x, y = find(x), find(y)
            parent[x] = y
            return x != y

        for s in sets:
            if not s:
                continue
            x = s[0]
            for y in s[1:]:
                union(x, y)
        res = 0
        for i in parent:
            if parent[i] == i:
                res += 1
        # print parent
        return res


############ test case ###########
s = Solution()
print s.setUnion([[1, 2, 3], [3, 9, 7], [4, 5, 10]])
