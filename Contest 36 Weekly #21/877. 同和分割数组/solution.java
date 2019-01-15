// 给定一个有n个整数的数组，需要找到满足以下条件的三胞胎(i, j, k):
// 0 < i, i + 1 < j, j + 1 < k < n - 1
// 每个子数组的和(0,i - 1)， (i + 1, j - 1)， (j + 1, k - 1)和(k + 1, n - 1)应该相等。
// 我们定义子数组(L, R)表示原始数组从元素索引L到元素索引R的一部分。

// 在线评测地址: http://www.lintcode.com/problem/split-array-with-equal-sum/


public class Solution {
    /**
     * @param nums: a list of integer
     * @return: return a boolean
     */
    public boolean splitArray(List<Integer> nums) {
        int[] prefixSum = new int[nums.size() + 1];
        for (int i = 1; i <= nums.size(); i++) {
            prefixSum[i] = prefixSum[i - 1] + nums.get(i - 1);
        }

        for (int i = 1; i < nums.size(); i++) {
            int j = i + 1;
            int count = 0;
            int cur = 0;
            int tar = prefixSum[i];
            while (j < nums.size() && count < 2) {
                cur += nums.get(j);
                if (cur == tar) {
                    cur = 0;
                    count++;
                    j++;
                }
                j++;
            }

            if (j < nums.size() && count == 2
                && tar == prefixSum[prefixSum.length -1] - prefixSum[j]) {
                return true;
            }
        }
        return false;
    }
}
