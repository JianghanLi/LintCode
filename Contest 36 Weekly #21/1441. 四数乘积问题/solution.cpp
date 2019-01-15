class Solution {
public:
    /**
     * @param n: The length of the array
     * @param a: Known array
     * @param k: The product of the selected four numbers cannot be greater than k
     * @return: The number of legal plan
     */

    int sum[1000000+10],cnt[1000000+10];

    long long numofplan(int n, vector<int> &a, int k) {
        // Write your code here

        //Init
        for (int i = 0; i <= k; i++) {
            sum[i] = cnt[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            if (a[i] > k) {
                continue;
            }
            cnt[a[i]]++;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (a[i] * a[j] > k) {
                    continue;
                }
                sum[a[i] * a[j]]++;
            }
        }
        for (int i = 1; i <= k; i++) {
            cnt[i] += cnt[i-1];
            sum[i] += sum[i-1];
        }

        long long ans = 0;
        for (int i = 0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                int res = a[i] * a[j];
                if (res > k) {
                    continue;
                }
                res = k / res;
                ans += sum[res];
                if (a[i] <= res) {
                    ans -= cnt[res / a[i]];
                    if (a[i] <= res / a[i]) {
                        ans++;
                    }
                }
                if (a[j] <= res) {
                    ans -= cnt[res / a[j]];
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
};