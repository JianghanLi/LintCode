class Solution {
public:
    /**
     * @param array: a 2D array
     * @return: the minimum difference
     */
    struct node
    {
        int x, y, v;
        node(int x, int y, int v) : x(x), y(y), v(v){}
        bool operator > (const node &rhs) const
        {
            return v > rhs.v || v == rhs.v && y > rhs.y;
        }
    };

    int minimumDifference(vector<vector<int>> &array) {
        // Write your code here
        if(array.empty()) return 0;
        int n = array.size(), m = array[0].size();

        vector<int> a(n, 0);
        int ans = INT_MAX, least = INT_MAX, most = INT_MIN;
        priority_queue<node, vector<node>, std::greater<node>> pq;

        //push first column
        for( int i = 0; i < n; i++)
        {
            pq.push({i, 0, array[i][0]});
            least = min(least, array[i][0]);
            most = max(most, array[i][0]);
        }
        while(!pq.empty())
        {
            node t = pq.top();
            pq.pop();
            least = t.v;
            ans = min(ans, most - least);
            if(t.y == m - 1) return ans;
            t.y++;
            t.v = array[t.x][t.y];
            most = max(most, t.v);
            pq.push(t);
        }
        return ans;
    }
};