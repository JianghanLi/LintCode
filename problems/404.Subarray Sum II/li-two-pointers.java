public class Solution {
    /**
     * @param A: An integer array
     * @param start: An integer
     * @param end: An integer
     * @return: the number of possible answer
     */
    public int subarraySumII(int[] A, int start, int end) {
       return atMostK(A, end) - atMostK(A, start - 1);
    }
    
    public int atMostK(int[] A, int K) {
        int i = 0, res = 0, cur = 0;
        for (int j = 0; j < A.length; ++j) {
            cur += A[j];
            while (cur > K && cur > 0) cur -= A[i++];
            res += j - i;
        }
        return res;
    }
}