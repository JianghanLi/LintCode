/**
* 本参考程序来自九章算法，由 @华助教 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

class SegmentTree {
    public int start, end;
    public int sum;
    public SegmentTree left, right;

    public SegmentTree(int start, int end) {
        this.start = start;
        this.end = end;
        this.left = this.right = null;
    }

    public SegmentTree(int start, int end, int sum) {
        this(start, end);
        this.sum = sum;
    }

    public static SegmentTree build(int start, int end) {
        if (start > end)
            return null;

        if (start == end) {
            return new SegmentTree(start, end, 1);
        }

        SegmentTree node = new SegmentTree(start, end, 1);
        int mid = (start + end) / 2;
        node.left = build(start, mid);
        node.right = build(mid + 1, end);
        node.sum = 0;

        if (node.left != null) {
            node.sum += node.left.sum;
        }
        if (node.right != null) {
            node.sum += node.right.sum;
        }
        return node;
    }

    public static int query(SegmentTree root, int k) {
        if (root.start > root.end)
            return 0;

        if (root.start == root.end) {
            root.sum = 0;
            return root.start;
        }

        int mid = (root.start + root.end) / 2;
        int res = 0;
        if (k <= root.left.sum) {
            res = query(root.left, k);
        } else {
            res = query(root.right, k - root.left.sum);
        }

        root.sum = 0;
        if (root.left != null) {
            root.sum += root.left.sum;
        }
        if (root.right != null) {
            root.sum += root.right.sum;
        }
        return res;
    }
}

class Num {
    int val;  //The value of numbers
    int cnt;  //How many numbers small than itself

    Num(int val, int cnt){
        this.val = val;
        this.cnt = cnt;
    }
}

class Cmp implements Comparator<Num> {
    //  delimit how to compare
    public int compare(Num a, Num b) {
        if (a.val < b.val) {
            return 1;
        } else {
            return -1;
        }
    }
}

public class Solution {
    /**
     * @param n: The array sum
     * @param arr1: The size
     * @param arr2: How many numbers small than itself
     * @return: The correct array
     */
    static Num[] a = new Num[100000+10];

    public int[] getQueue(int n, int[] arr1, int[] arr2) {
        int[] ans = new int[n];
        // Write your code here
        for (int i = 0; i < n; i++) {
            a[i] = new Num(arr1[i], arr2[i]);
        }


        Arrays.sort(a, 0, n, new Cmp());
        SegmentTree root = SegmentTree.build(1,n);


        for (int i = 0; i < n; i++) {
            int pos = SegmentTree.query(root, a[i].cnt+1);
            ans[pos-1] = a[i].val;
        }
        return ans;
    }
}