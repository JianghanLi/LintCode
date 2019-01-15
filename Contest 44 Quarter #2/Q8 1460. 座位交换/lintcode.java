public class Solution {
    /**
     * @param n: The number of seats
     * @param arr: The number of peaple come or leave
     * @return: The answer array
     */
    public List<Integer> arrangeSeat(int n, List<Integer> arr) {
        // Write your code here
        List<Integer> ret = new ArrayList<>();
        if (arr == null || arr.size() == 0) {
            return ret;
        }
        if (n <= 0) {
            for (int ele : arr) {
                ret.add(-1);
            }
            return ret;
        }

        // n > 0
        int[] nums = new int[n];
        Map<Integer, Integer> hash = new HashMap<>();
        for (int ele : arr) {
            ret.add(getSeat(ele, nums, hash));
        }
        return ret;
    }

    private int getSeat(int x, int[] nums, Map<Integer, Integer> hash) {
        if (x <= 0) {
            Integer pos = hash.get(-x);
            if (pos == null) {
                return -1;
            }
            nums[pos] = 0;
            hash.remove(-x);
            return 1;
        }
        // x is positive;
        int len = nums.length;
        int ret = -1;
        int retDist = 0;

        if (nums[0] == 0) {
            int ipos = 1;
            for (; ipos < len; ipos++) {
                if (nums[ipos] > 0) {
                    break;
                }
            }
            if (ipos < len) {
                ret = 0;
                retDist = ipos;
            } else {
                nums[0] = x;
                hash.put(x, 0);
                return 0;
            }
        }

        int prev1 = -1;
        for (int i = 0; i < len; i++) {
            if (nums[i] > 0) {
                if (prev1 != -1) {
                    if (i > prev1 + 1) {
                        int curDist = (i - prev1) / 2;
                        int curRet = prev1 + curDist;
                        if (curDist > retDist) {
                            ret = curRet;
                            retDist = curDist;
                        }
                    }
                }
                prev1 = i;
            }
        }

        if (nums[len - 1] == 0) {
            int ipos = len - 2;
            for (; ipos >= 0; ipos--) {
                if (nums[ipos] > 0) {
                    break;
                }
            }
            int curDist = len - 1 - ipos;
            if (curDist > retDist) {
                ret = len - 1;
                retDist = curDist;
            }
        }
        if (ret == -1) {
            return ret;
        }
        hash.put(x, ret);
        nums[ret] = x;
        return ret;
    }
}