typedef long long LL;

class Solution {
public:
    /**
     * @param s: The capacity of backpack
     * @param v: The value of goods
     * @param c: The capacity of goods
     * @return: The answer
     */
    long long getMaxValue(int s, vector<int> &v, vector<int> &c)
    {
        int n = v.size();
        int W = s;
        int N = n+1;
        pair <LL, LL> pi[1 << (N / 2)];
        vector<int>w=c;

        // 前n/2个数的任意组合后的结果，存入list
        int n2 = n / 2;
        for(int i = 0; i < (1 << n2); i++) {
            LL sw = 0, sv = 0;
            for(int j = 0; j < n2; j++) {
                if((i >> j) & 1) {
                    sw += w[j];
                    sv += v[j];
                }
            }
            pi[i] = make_pair(sw, sv);
        }

        // cleanup，找到weight, value同时递增的组合。
        sort(pi, pi + (1 << n2));
        int m = 1;
        for(int i = 1; i < (1 << n2); i++) {
            if(pi[m-1].second < pi[i].second) {
                pi[m++] = pi[i];
            }
        }
        // (N/2)*2^(N/2)
        LL res = 0;
        for(int i = 0; i < (1 << (n - n2)); i++) {
            LL sw = 0, sv = 0;
            for(int j = 0; j < n - n2; j++) {
                if((i >> j) & 1) {
                    sw += w[n2 + j];
                    sv += v[n2 + j];
                }
            }
            if(sw <= W) {
                LL tv = (lower_bound(pi, pi + m, make_pair(W - sw +1, 0LL)) - 1)->second;
                res = max(res, sv + tv);
            }
        }

        return res;
    }
};