import java.util.*;

class Solution {
    public int[] getQueue(int n, int[] arr1, int[] arr2) {
        int[][] a = new int[n][2];
        for (int i = 0; i < n; i++) {
            a[i][0] = arr1[i];
            a[i][1] = arr2[i];
        }
        Arrays.sort(a, (x, y) -> (x[0] - y[0]));
        List<Integer> res = new LinkedList<Integer>();
        for (int i = 0; i < n; i++) res.add(a[i][1], a[i][0]);
        // int[] res2 = new int[n];
        // for (int i = 0; i < n; i++) res2[i] = res.get(i);
        return res.stream().mapToInt(i -> i).toArray();
    }
}
/********************* test case *********************/

class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.getQueue(5, new int[] {1, 2, 3, 4, 5}, new int[] {0, 0, 0, 1, 3})));
    }
}