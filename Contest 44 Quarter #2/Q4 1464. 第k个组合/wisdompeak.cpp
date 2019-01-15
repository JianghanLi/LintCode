class Solution {
public:
    /**
     * @param n: The integer n
     * @param k: The integer k
     * @return: Return the combination
     */
    vector<int> getCombination(int n, int k) {
        set<int>Set;
        for (int i = 1; i <= n; i++)
            Set.insert(i);

        vector<int>result;

        DFS(n, k, result, Set);

        return result;
    }

    void DFS(int n, int k, vector<int>& result, set<int>& Set) {
        if (k == 0) {
            //cout<<"Hi"<<" "<<result.size()<<endl;

            vector<int>temp;
            while (Set.size() > n / 2 - result.size())
                Set.erase(*Set.begin());

            for (auto a : Set)
                result.push_back(a);

            return;
        }

        int a = result.size();
        int b = Set.size() - 1;


        while (k >= 0) {
            long long comb = combinator(b, n / 2 - a - 1);
            //cout<<"comb="<<comb<<endl;

            if (k == comb) {
                result.push_back(*Set.begin());
                Set.erase(*Set.begin());
                k = 0;
                break;
            }
            else if (k > comb) {
                k = k - comb;
                Set.erase(*Set.begin());
                b--;
            }
            else if (k < comb) {
                result.push_back(*Set.begin());
                Set.erase(*Set.begin());
                break;
            }

        }

        DFS(n, k, result, Set);


    }


    long factorial(long number) {
        if (number <= 1)
            return 1;
        else
            return number * factorial(number - 1);
    }

    int combinator(int n, int m) {
        int temp;
        if (n < m) {
            temp = n;
            n = m;
            m = temp;

        }
        return factorial(n) / (factorial(m) * factorial(n - m));
    }
};