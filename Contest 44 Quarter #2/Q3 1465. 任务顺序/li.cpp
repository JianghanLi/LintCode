#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    /**
     * @param n: The number of tasks
     * @param t: The time array t
     * @param p: The probability array p
     * @return: Return the order
     */
    vector<int> getOrder(int n, vector<int> t, vector<double> p) {
        vector<pair<double, int>> v;
        for (int i = 0; i < n; ++i)
            v.push_back({ -(double)p[i] / t[i], i + 1});
        sort(v.begin(), v.end());
        vector<int> res;
        for (int i = 0; i < n; ++i)
            res.push_back(v[i].second);
        return res;
    }
};

/********************* test case *********************/
int main() {
    Solution s;
    // for (int i : s.getOrder(2, {1, 2}, {0.3, 0.7}))
    //     cout << i << " ";
    double a = 2/0.2;
    double b = 0.7/7;
    double c = 0.1;
    cout << a << endl;
    cout << b << endl;
    cout << (a == b) << endl;
    cout << (a == c) << endl;
    cout << (b == c) << endl;
}