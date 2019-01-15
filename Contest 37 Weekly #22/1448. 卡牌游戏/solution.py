# 本参考程序来自九章算法，由 @邓助教 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param n: The number of cards
    @param totalProfit: The totalProfit
    @param totalCost: The totalCost
    @param a: The profit of cards
    @param b: The cost of cards
    @return: Return the number of legal plan
    """
    def numOfPlan(self, n, totalProfit, totalCost, a, b):
        # Write your code here
        dp = [[0 for j in range(110)] for i in range(110)]
        dp[0][0] = 1
        mod = 1000000007
        for i in range(n):
            for j in range(totalProfit + 1, -1, -1):
                for k in range(totalCost + 1, -1, -1):
                    idxA = min(totalProfit + 1, j + a[i])
                    idxB = min(totalCost + 1, k + b[i])
                    dp[idxA][idxB] = (dp[j][k] + dp[idxA][idxB]) % mod
        ans = 0
        for i in range(totalCost):
            ans = (ans + dp[totalProfit + 1][i]) % mod
        return ans

# https://www.lintcode.com/problem/card-game/description

# https://www.jiuzhang.com/solution/card-game/#tag-highlight-lang-java

# 假设dp[i][j]dp[i][j]为卡牌利润和等于ii且成本和等于jj的方案数。 则按顺序枚举每一个卡牌xx，同时更新dpdp数组，有： dp[i+a[x]][j+b[x]] += dp[i][j]dp[i+a[x]][j+b[x]]+=dp[i][j]

# 时间复杂度：O(n * totalProfit * totalCost)O(n∗totalProfit∗totalCost)
