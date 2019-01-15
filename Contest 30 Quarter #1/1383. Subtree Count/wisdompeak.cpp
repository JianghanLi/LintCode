class Solution {
public:
    /**
     * @param start: The start of the edges set
     * @param end: The end of the edges set
     * @return: Return the subtree count
     */
    int getSubtreeCount(vector<int> &start, vector<int> &end)
    {
        unordered_map<int,vector<int>>Map;
        for (int i=0; i<start.size(); i++)
        {
            Map[start[i]].push_back(end[i]);
        }
        unordered_map<int,long long>counts;
        long long M = 10000007;
        long long temp = DFS(1,Map,counts);
        long long result = 0;
        for (auto a:counts)
        {
            result += a.second;
            result = result % M;
        }
        return result;

    }

    long long DFS(int root, unordered_map<int,vector<int>>&Map, unordered_map<int,long long>&counts)
    {
        if (Map.find(root)==Map.end())
        {
            counts[root]=1;
            return 1;
        }


        long long result = 1;
        long long M = 10000007;
        for (int i=0; i<Map[root].size(); i++)
        {
            result = result*(DFS(Map[root][i],Map,counts)%M+1);
            result = result%M;
        }
        counts[root]=result;
        return result;
    }
};