public class Solution {
    /**
     * @param array: a 2D array
     * @return: the minimum difference
     */
    class Pair implements Comparable<Pair>{
        int x, y, val;
        public Pair(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }

        public int compareTo(Pair o) {
            return this.val - o.val;
        }
    }
    public int minimumDifference(int[][] array) {
        // Write your code here
        int max = Integer.MIN_VALUE;
        int m = array.length;
        int n = array[0].length;
        int ans = Integer.MAX_VALUE;
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        for(int i = 0; i < m; i ++) {
            max = Math.max(max, array[i][0]);
            pq.offer(new Pair(i, 0, array[i][0]));
        }
        while(!pq.isEmpty()) {
            Pair min = pq.poll();
            int x = min.x;
            int y = min.y;
            ans = Math.min(ans, max - min.val);
            if(y + 1 == n) break;
            pq.offer(new Pair(x, y + 1, array[x][y + 1]));
            max = Math.max(max, array[x][y + 1]);
        }
        return ans;
    }
}