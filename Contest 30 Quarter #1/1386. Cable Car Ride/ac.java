// LC 329
public class Solution {
    /**
     * @param height: the Cable car station height
     * @return: the longest time that he can ride
     */
    private final int[][] DIR = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

    public  int cableCarRide(int[][] height) {
        if (height == null || height.length == 0 || height[0] == null || height[0].length == 0) {
            return 0;
        }

        int m = height.length;
        int n = height[0].length;
        int result = 0;

        int[][] cache = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result = Math.max(result, helper(height, cache, i, j));
            }
        }

        return result;
    }

    private int helper(int[][] height, int[][] cache, int i, int j) {
        if (cache[i][j] != 0) {
            return cache[i][j];
        }

        for (int[] dir: DIR) {
            int x = i + dir[0];
            int y = j + dir[1];

            if (x < 0 || y < 0 || x >= height.length || y >= height[0].length) {
                continue;
            }

            if (height[x][y] > height[i][j]) {
                cache[i][j] = Math.max(cache[i][j], helper(height, cache, x, y));
            }
        }

        cache[i][j]++;
        return cache[i][j];

    }
}