// 解答来自LeetCode， 本题是把array 分为四个部分，是通过抽掉三个数来实现的

// for loop 先遍历中间那个抽掉的数，从 i = 3 -> nums.size()-3 左右要至少预留三个数

// 在for loop 内建立一个set，

// 然后对左半部分处理，for loop 抽掉一个数，看其左右两部分和是否相等，相等的话把该值放入set中
// 遍历完左半部分后， 对右侧进行for loop 遍历，右侧抽掉一个数，看其左右是否相等，然后再看这个等值是否在set出现，出现过返回true


public class Solution {
    /**
     * @param nums: a list of integer
     * @return: return a boolean
     */
    public boolean splitArray(List<Integer> nums) {
        // write your code here
        if(nums == null || nums.size() < 6){
            return false;
        }

        int[] sum = new int[nums.size() + 1];
        sum[0] = 0;
        for(int i = 1; i < sum.length; i++){
            sum[i] = sum[i - 1] + nums.get(i - 1);
        }
        for(int i = 3; i < nums.size() - 3; i++){
            Set<Integer> set = new HashSet<>();
            for(int j = 1; j < i - 1; j++){
                if(sum[j] == sum[i] - sum[j + 1]){
                    if(!set.contains(sum[j]))
                    set.add(sum[j]);
                }
            }

            for(int k = i + 2; k < nums.size() - 1; k++){
                if(sum[k] - sum[i + 1] == sum[nums.size()] - sum[k + 1]){
                    if(set.contains(sum[k] - sum[i + 1])){
                        return true;
                    }
                }
            }
        }

        return false;
    }
}