class Solution {
public:
    /**
     * @param s: The string
     * @param k: The longest length of the substring
     * @return: Returns the lexicographically smallest string
     */


    string getMinString(string &s, int k)
    {

        int N = s.size();

        string str=s;
        sort(str.begin(),str.end());
        int m=0;
        while (m<s.size() && s[m]==str[m])
            m++;


        string part1 = s.substr(0,m);

        string result = s.substr(m);

        for (int l1 = 1; l1<=k; l1++)
        {
            if (m+k>N) break;
            for (int j=m+l1; j<N; j++)
                for (int l2=1; l2<=k; l2++)
                {
                    if (j+l2>N) break;
                    result = min(result, s.substr(j,l2)+s.substr(m+l1,j-m-l1)+s.substr(m,l1)+s.substr(j+l2));
                }
        }

        return part1+result;


    }
};