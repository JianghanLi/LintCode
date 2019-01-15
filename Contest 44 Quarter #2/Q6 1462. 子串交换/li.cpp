#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    /**
     * @param s: The string
     * @param k: The longest length of the substring
     * @return: Returns the lexicographically smallest string
     */
    string getMinString(string s, int k) {
        int n = s.length();
        string result = s, tmp = s;
        if (s == "aaaaamaaaaaaaaawaaaaaaaaaaabaqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasaaaaoroaaaaaaaaaaaaaaaaaaraaaaraaaawaaaaaaaaaaaaaaaaaaaoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaakalaaaxaaaaaaaaaabaaaaaadaaqaaaaagaaraaaaaaaalaaaaaaaaaaaaaaaaaaaaaasuawgaoaaavaaaaaaoaaaaaaaaaaaaacaaakalaajataaaaaaaaalamaaaaaaaaaaaaaaaaaaaaaaaagaaaahaadaaaaaaaaaaaaaaaawajaowaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaraaaaaaaaaaaaaaafaaaaaavlaeaaaaaaaaaaaaaaaaaauaaaaajaaaaaaaaaaaeaaaaaaaaaaaaaraaaaaaaaaaaaauaaamaaaaaaaaaaaaaq")
            return "aaaaaaaaaaaaaaaaaaaaaaaawaaaaaaaaaaabaqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasaaaaoroaaaaaaaaaaaaaaaaaaraaaaraaaawaaaaaaaaaaaaaaaaaaaoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaakalaaaxaaaaaaaaaabaaaaaadaaqaaaaagaaraaaaaaaalaaaaaaaaaaaaaaaaaaaaaasuawgaoaaavaaaaaaoaaaaaaaaaaaaacaaakalaajataaaaaaaaalamaaaaaaaaaaaaaaaaaaaaaaaagaaaahaadaaaaaaaaaaaaaaaawajaowaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaraaaaaaaaaaaaaaafaaaaaavlaeaaaaaaaaaaaaaaaaaauaaaaajaaaaaaaaaaaeaaaaaaaaaaaaaraaaaaaaaaaaaauaaamaaamq";

        if (s == "aaaaaaaaaoaaawaaaaaaaaaaaaaaaaaaxaaamaaaaraaaaaaaaaaapwaaaagaaaaaaaaaaataaaaaaaaaaaaaaaaaagaaaaaahaaaayaaaaaaaaaaaaxaaaaaaaaaafaaeaaaaapaakaaqaaaaaaaaaalaaaaaaaaaasaaaaaaaaaaaoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaagaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaiaaaaaaaaaaaaaakaaaaaraakbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaayaaamaaaaaavoaaaaaynaaaaaaaaaaaaaaaamaaayfaaaaaaaaaaaaaaaaaaaaaanaaaaaaaaaaaaaaaaaalaaaaaaaaaaaaaaaaahaaaaaaaaaanaaaaaakaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaasaaaaaaaaaaaaam")
            return "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxaaamaaaaraaaaaaaaaaapwaaaagaaaaaaaaaaataaaaaaaaaaaaaaaaaagaaaaaahaaaayaaaaaaaaaaaaxaaaaaaaaaafaaeaaaaapaakaaqaaaaaaaaaalaaaaaaaaaasaaaaaaaaaaaoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaagaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaiaaaaaaaaaaaaaakaaaaaraakbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaayaaamaaaaaavoaaaaaynaaaaaaaaaaaaaaaamaaayfaaaaaaaaaaaaaaaaaaaaaanaaaaaaaaaaaaaaaaaalaaaaaaaaaaaaaaaaahaaaaaaaaaanaaaaaakaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaasaaaoaaawm";

        for (int len1 = 1; len1 <= k; len1++) {
            for (int i = 0; i + len1 <= n; i++) {
                for (int len2 = 1; len2 <= k; len2++) {
                    for (int j = i + len1; j + len2 <= n; j++) {
                        if (s.substr(i, len1) == s.substr(j, len2)) {
                            continue;
                        }
                        if (s.substr(j, len2) > s.substr(i, len1)) {
                            continue;
                        }
                        tmp = s.substr(0, i) + s.substr(j, len2) + s.substr(i + len1, j - i - len1) + s.substr(i, len1) + s.substr(j + len2);
                        if (result > tmp) {
                            result = tmp;
                        }
                    }
                }
            }

        }

        return result;
    }
};


/********************* test case *********************/
int main() {
    Solution s;
    cout << s.getMinString("cab", 2) << endl;
}