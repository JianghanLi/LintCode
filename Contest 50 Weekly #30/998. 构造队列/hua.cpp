/**
* 本参考程序来自九章算法，由 @华助教 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

class SegmentTree{
public:
    int start, end;
    long long sum;
    SegmentTree *left, *right;
    SegmentTree(int start, int end, long long sum = 0): start(start),end(end),sum(sum){};

    static SegmentTree *build(int start, int end) {
        if (start > end) return nullptr;
        SegmentTree *head = new SegmentTree(start, end, 1);
        if (start == end) return head;
        int mid = (start + end) /2;
        head->left = build(start, mid);
        head->right = build(mid+1, end);
        head->sum = 0;
        if (head->left)
            head->sum +=  head->left->sum;
        if (head->right)
            head->sum +=  head->right->sum;
        return head;
    }

    static int query(SegmentTree *head, int value) {
        if (head->start  ==  head->end) {
            head->sum = 0 ;
            return head->start;
        }
        int mid = (head->start + head->end) /2;
        int re;
        int tmp = head->left->sum;
        if (value <= tmp ) {
             re = query(head->left,value);
        }
        else  {
             re = query(head->right,value-tmp);
        }
        head->sum = 0;
        if (head->left)
            head->sum += head->left->sum;
        if (head->right)
            head->sum += head->right->sum;
        return re;
    }
};

class Solution {
public:
    /**
     * @param n: The array sum
     * @param arr1: The size
     * @param arr2: How many numbers small than itself
     * @return: The correct array
     */
     SegmentTree *head;
      struct Node{
        int num,ss;
    }a[105000];
    int ans[105000];
    static int cmp1(Node a,Node b){
        return a.num > b.num;
    }
    vector<int> getQueue(int n, vector<int> &arr1, vector<int> &arr2) {
         vector<int> ans1;
            int i;
            for (i = 0;i < n;i++) a[i+1].num = arr1[i];
            for (i = 0;i < n;i++) a[i+1].ss = arr2[i];
            sort(a+1,a+1+n,cmp1);
            memset(ans,0,sizeof(ans));
            head = SegmentTree::build(1,n);
            for (i = 1;i <= n;i++) {
                ans[SegmentTree::query(head,a[i].ss+1)] = a[i].num;
            }
            ans1.clear();
            for (i = 1;i <= n;i++) {
            ans1.push_back(ans[i]);
            }
            return ans1;
    }
};