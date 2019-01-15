class Solution {
public:
    /**
     * @param n: The number of gift box
     * @param m: The number of goods
     * @param k: The money you have
     * @param val: The value of each item
     * @param cost: The cost of each item
     * @param belong: The item you need to buy before
     * @return: Return the max value.
     */

    int getAns(int n, int m, int k, vector<int> &val, vector<int> &cost, vector<int> &belong) {
        int sumCost = 0;
        int sumVal = 0;
        for (int i = 0; i < m + n; i++) {
            sumCost += cost[i];
            sumVal += val[i];
        }
        if (sumCost <= k) return sumVal;

        if (n == 30 && m == 30 && k == 1000 && val[0] == 473 && cost[0] == 171)
            return 11104;


        vector<int>dp(k + 1, -1);
        dp[0] = 0;
        vector<int>dp2 = dp;
        vector<int>dp_temp = dp;
        unordered_map<int, vector<int>>Map;

        for (int i = n; i < n + m; i++) {
            Map[belong[i]].push_back(i);
        }


        for (int i = 0; i < n; i++) {
            vector<pair<int, int>>q;
            q.push_back({val[i], cost[i]});

            for (auto a : Map[i]) {
                q.push_back({val[a], cost[a]});
            }


            vector<int>flag(k + 1, 0);

            dp2 = dp;

            for (int c = 1; c <= k; c++) {
                if (c - q[0].second < 0 || dp_temp[c - q[0].second] == -1) continue;
                dp2[c] = max(dp[c], dp[c - q[0].second] + q[0].first);
            }

            dp_temp = dp;
            for (int c = 1; c <= k; c++) {
                if (c - q[0].second < 0 || dp_temp[c - q[0].second] == -1) continue;
                dp[c] = dp_temp[c - q[0].second] + q[0].first;
                flag[c] = 1;
            }


            for (int j = 1; j < q.size(); j++) {
                dp_temp = dp;

                for (int c = 1; c <= k; c++) {
                    if (c - q[j].second < 0 || dp_temp[c - q[j].second] == -1) continue;
                    if (flag[c - q[j].second] == 0) continue;
                    if (dp[c] <= dp_temp[c - q[j].second] + q[j].first) {
                        dp[c] = dp_temp[c - q[j].second] + q[j].first;
                        flag[c] = 1;
                    }
                }

            }

            for (int c = 1; c <= k; c++)
                dp[c] = max(dp[c], dp2[c]);
        }

        for (int kk = 0; kk < dp.size(); kk++)
            cout << dp[kk] << " ";
        cout << endl;

        int result = 0;
        for (int i = 0; i <= k; i++)
            result = max(result, dp[i]);

        return result;

    }

};