#include <bits/stdc++.h>
using namespace std;


// 2366 ms
class Solution {
public:
    /**
     * @param n: The array sum
     * @param arr1: The size
     * @param arr2: How many numbers small than itself
     * @return: The correct array
     */
    vector<int> getQueue(int n, vector<int> arr1, vector<int> arr2) {
        vector<vector<int>> a;
        for (int i = 0; i < n; ++i)
            a.push_back({arr1[i], arr2[i]});
        sort(a.begin(), a.end());
        vector<int> res;
        for (int i = 0; i < n; ++i)
            res.insert(res.begin() + a[i][1], a[i][0]);
        return res;
    }
};

/********************* test case *********************/
int main() {
    Solution s;
    for (int i : s.getQueue(5, {1, 2, 3, 4, 5}, {0, 0, 0, 1, 3})) cout << i << " ";
    cout << endl;
}