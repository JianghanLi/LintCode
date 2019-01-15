/**
* 本参考程序来自九章算法，由 @邓助教 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

public class Solution
{
    /**
     * @param n: The number of cards
     * @param totalProfit: The totalProfit
     * @param totalCost: The totalCost
     * @param a: The profit of cards
     * @param b: The cost of cards
     * @return: Return the number of legal plan
     */
    public int numOfPlan(int n, int totalProfit, int totalCost, int[] a, int[] b) {
        // Write your code here
        long mod = 1000000007;
        long [][][]dp;
        dp = new long [150][150][150];
        int i, j, k;
        for (i = 0; i <= 105; i++)
            for (j = 0; j <= 105; j++)
                for (k = 0; k <= 105; k++) {
                    dp[i][j][k] = 0;
                }
        dp[0][0][0] = 1;
        for (k = 0; k < n; k++)
            for (i = 0; i <= totalProfit + 1; i++)
                for (j = 0; j < totalCost; j++)
                  if (dp[k][i][j] > 0) {
                        dp[k + 1][i][j] += dp[k][i][j];
                        dp[k + 1][i][j] %= mod;
                        if (j + b[k] < totalCost) {
                            dp[k + 1][Math.min(totalProfit + 1, i + a[k])][j + b[k]] += dp[k][i][j];
                            dp[k + 1][Math.min(totalProfit + 1, i + a[k])][j + b[k]] %= mod;
                        }
                    }
        long sum;
        sum = 0;
        for (j = 0; j < totalCost; j++) {
            sum = (sum + dp[n][totalProfit + 1][j]) % mod;
        }
        return (int)sum;
    }
}