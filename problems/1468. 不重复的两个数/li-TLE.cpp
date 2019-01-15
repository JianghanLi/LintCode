#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    /**
     * @param a: the array
     * @return: the two numbers that are not repeated
     */
    vector<int> theTwoNumbers(vector<int> a) {
        unordered_set<int> s;
        for (int & i : a)
            if (s.count(i)) s.erase(i);
            else s.insert(i);
        vector<int> v;
        for (int i : s) v.push_back(i);
        if (v[0] > v[1]) swap(v[0], v[1]);
        return v;
    }
};

/********************* test case *********************/
int main() {
    Solution s;

    for (int i: s.theTwoNumbers({1, 2, 5, 5, 6, 6}))
        cout << i << " ";
}