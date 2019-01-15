import java.util.*;

class Solution {
    /**
     * @param arr: The release order
     * @param n: The cooldown
     * @return: Return the time
     */
    public int askForCoolingTime(int[] arr, int n) {
        // Write your code here
        HashMap<Integer, Integer> m = new HashMap<>();
        int cur = 0;
        for (int i : arr) {
            cur  = Math.max(m.getOrDefault(i, -n) + n, cur) + 1;
            m.put(i, cur);
        }
        return cur;
    }
}

/********************* test case *********************/

class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
    }
}