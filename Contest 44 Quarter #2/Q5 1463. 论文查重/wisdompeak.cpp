class Solution {
public:
    /**
     * @param words1: the words in paper1
     * @param words2: the words in paper2
     * @param pairs: the similar words pair
     * @return: the similarity of the two papers
     */
    unordered_map<string,string>Father;

    float getSimilarity(vector<string> &words1, vector<string> &words2, vector<vector<string>> &pairs)
    {
        int M = words1.size();
        int N = words2.size();

        for (int i=0; i<words1.size(); i++)
            Father[words1[i]] = words1[i];

        for (int i=0; i<words2.size(); i++)
            Father[words2[i]] = words2[i];

        for (int i=0; i<pairs.size(); i++)
        {
            Father[pairs[i][0]] = pairs[i][0];
            Father[pairs[i][1]] = pairs[i][1];
        }

        for (int i=0; i<pairs.size(); i++)
        {
            if (findFather(pairs[i][0])!=findFather(pairs[i][1]))
                Union(pairs[i][0],pairs[i][1]);
        }

        words1.insert(words1.begin(),"");
        words2.insert(words2.begin(),"");
        auto dp = vector<vector<int>>(M+1,vector<int>(N+1,0));
        for (int i=0; i<=M; i++) dp[i][0] = 0;
        for (int j=0; j<=N; j++) dp[0][j] = 0;

        for (int i=1; i<=M; i++)
            for (int j=1; j<=N; j++)
            {
                if (findFather(words1[i])==findFather(words2[j]))
                    dp[i][j] = dp[i-1][j-1]+1;
                else
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        cout<<dp[M][N]<<" "<<M<<" "<<N<<endl;
        return dp[M][N]*2.0/(M+N);

    }

    string findFather(string x)
    {
        if (Father[x]!=x)
            Father[x] = findFather(Father[x]);
        return Father[x];
    }

    void Union(string x, string y)
    {
        x = Father[x];
        y = Father[y];
        if (x<=y)
            Father[y] = x;
        else
            Father[x] = y;
    }
};