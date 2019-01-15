class Solution {
public:
    /**
     * @param meeting: The meetings
     * @param pause: The pause time of meetings
     * @param query: The query
     * @return: Return the answer of each query
     */

    vector<int> getQuery(vector<vector<int>> &meeting, vector<vector<int>> &pause, vector<int> &query)
    {
        int N = meeting.size();
        int M = pause.size();

        unordered_map<int,vector<int>>MeetingPause;
        for (int i=0; i<pause.size(); i++)
            MeetingPause[pause[i][0]].push_back(i);


        vector<pair<int,int>>All;


        for (int i=0; i<N; i++)
        {
            vector<pair<int,int>>Set;
            Set.push_back({meeting[i][1],1});
            Set.push_back({meeting[i][2]+1,-1});

            for (int j: MeetingPause[meeting[i][0]])
            {
                Set.push_back({pause[j][1],-1});
                Set.push_back({pause[j][2]+1,1});
            }

            sort(Set.begin(),Set.end());


            int count=0;

            for (auto a:Set)
            {
                if (a.second==1)
                {
                    count+=1;
                    if (count>0)
                        All.push_back({a.first,1});
                }
                else
                {
                    count-=1;
                    if (count==0)
                        All.push_back({a.first,-1});
                }
            }
        }


        sort(All.begin(),All.end());


        map<int,int>Map;

        int count=0;
        for (int i=0; i<All.size(); i++ )
        {
            count+=All[i].second;
            Map[All[i].first]=count;
        }



        vector<int>result;
        for (int i=0; i<query.size(); i++)
        {
            auto it = Map.upper_bound(query[i]);
            if (it==Map.begin())
                result.push_back(0);
            else
            {
                it = prev(it,1);
                result.push_back(it->second);
            }

        }

        return result;

    }
};