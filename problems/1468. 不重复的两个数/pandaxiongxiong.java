public class Solution {
    /**
     * @param a: the array
     * @return: the two numbers that are not repeated
     */
    public List<Integer> theTwoNumbers(List<Integer> a) {
        // Write your code here
        int cur = 0;
        for(int num : a) {
            cur ^= num;
        }
        int lowbit = cur & (-cur);
        int res1 = 0;
        for(int num : a) {
            if((num & lowbit) != 0) {
                res1 ^=  num;
            }
        }
        int res2 = res1 ^ cur;
        if(res1 < res2) {
            return Arrays.asList(res1, res2);
        }
        return Arrays.asList(res2, res1);
    }
}

// https://www.lintcode.com/submission/15439278/