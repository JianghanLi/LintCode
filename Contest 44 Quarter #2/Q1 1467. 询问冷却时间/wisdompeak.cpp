class Solution {
public:
    /**
     * @param arr: The release order
     * @param n: The cooldown
     * @return: Return the time
     */
    int askForCoolingTime(vector<int> &arr, int n) {
        unordered_map<int, int>Map;
        int time = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (Map.find(arr[i]) == Map.end()) {
                Map[arr[i]] = time + n;
                time++;
            }
            else if (Map[arr[i]] < time) {
                Map[arr[i]] = time + n;
                time++;
            }
            else {
                time = Map[arr[i]] + 1;
                Map[arr[i]] = time + n;
                time++;
            }
        }
        return time;
    }
};