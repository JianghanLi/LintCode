/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param intervals: The intervals
     * @param k: The k
     * @return: The answer
     */
    int maximumLineCoverage(vector<Interval> &intervals, int k)
    {
        if (k==intervals.size())
        {
            vector<int>points(2001,0);
            for (int i=0; i<intervals.size(); i++)
            {
                for (int p=intervals[i].start; p<=intervals[i].end; p++)
                    points[p]=1;
            }
            int results=0;
            for (int i=1; i<=2000; i++)
                results+=points[i];
            return results;
        }


        sort(intervals.begin(),intervals.end(),[](const Interval &a, const Interval &b){ return a.start<b.start || a.start==b.start && a.end<b.end; });

        int N = intervals.size();
        auto dp = vector<vector<int>>(k+1,vector<int>(N,0));
        vector<int>Max(k+1,0);

        for (int i=0; i<N; i++)
        {
            dp[1][i] = intervals[i].end-intervals[i].start+1;
            Max[1]=max(Max[1],dp[1][i]);
        }


        for (int i=2; i<=k; i++)
        {
            for (int j=0; j<N; j++)
            {
                for (int k=j-1; k>=0; k--)
                {
                    if (dp[i-1][k]==INT_MIN)
                        continue;

                    if (intervals[k].end>intervals[j].end)
                    {
                        dp[i][j] = INT_MIN;
                        break;
                    }

                    if (intervals[k].end<intervals[j].start)
                        dp[i][j]=max(dp[i][j],dp[i-1][k]+intervals[j].end-intervals[j].start+1);
                    else
                        dp[i][j]=max(dp[i][j],dp[i-1][k]+intervals[j].end-intervals[k].end);

                    Max[i]=max(Max[i],dp[i][j]);

                    if (dp[i][j]==Max[i-1]+intervals[j].end-intervals[j].start+1)
                        break;

                }
                //cout<<i<<" "<<j<<" "<<dp[i][j]<<endl;
            }
        }

        int result=0;
        for (int i=1; i<=k; i++)
                result=max(result,Max[i]);

        return result;

    }
};