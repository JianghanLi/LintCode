public class Solution {
    /**
     * @param n: The length of the array
     * @param a: Known array
     * @param k: The product of the selected four numbers cannot be greater than k
     * @return: The number of legal plan
     */
    long [] num;
    long [] sum;

    public long numofplan(int n, int[] a, int k) {
        // Write your code here

        //Init
        num = new long [1000005];
        sum = new long [1000005];
        int i, j;
        for (i = 0; i <= k; i++) {
            sum[i] = num[i] = 0;
        }

        for (i = 0; i < n; i++) {
            if (a[i] > k) {
                continue;
            }
            num[a[i]]++;
        }
        for (i = 0; i < n; i++) {
            for (j = i + 1; j < n; j++) {
                if ((long)a[i] * a[j] > k) {
                    continue;
                }
                sum[a[i] * a[j]]++;
            }
        }
        for (i = 1; i <= k; i++) {
            num[i] += num[i - 1];
            sum[i] += sum[i - 1];
        }

        long ans = 0;
        for (i = 0; i < n; i++) {
            for(j = i + 1; j < n; j++) {
                long res = (long)a[i] * a[j];
                if (res > k) {
                    continue;
                }
                res = k / res;
                ans += sum[(int)res];
                if (a[i] <= res) {
                    ans -= num[(int)res / a[i]];
                    if (a[i] <= res / a[i]) {
                        ans++;
                    }
                }
                if (a[j] <= res) {
                    ans -= num[(int)res / a[j]];
                    if(a[j] <= res / a[j]) {
                        ans++;
                    }
                }
                if (a[i] * a[j] <= res) {
                    ans++;
                }
            }
        }
        ans /= 6;
        return ans;
    }
}