#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    /**
     * @param a: the array
     * @return: the two numbers that are not repeated
     */
    vector<int> theTwoNumbers(vector<int> &a) {
        int x = 0, x2 = 0;
        for (int i : a) x ^= i;
        int lowbit = x & -x;
        for (int i : a)
            if (i & lowbit)
                x2 ^= i;
        return {x2, x ^ x2};
    }
};
/********************* test case *********************/
int main() {
    Solution s;
    vector<int> a  = {1, 2};
    for (int i : s.theTwoNumbers(a))
        cout << i << endl;
}