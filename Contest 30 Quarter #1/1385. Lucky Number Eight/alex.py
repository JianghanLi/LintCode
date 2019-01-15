class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        # Write your code here
        if n < 8:
            return 0
        d = len(str(n)) - 1
        a = [0, 1]
        for i in xrange(2, d + 1):
            a.append(a[-1] * 9 + 10**(i - 1))

        p = 10**d
        m = n / p
        if m == 8:
            return m * a[d] + (n % p) + 1
        elif m > 8:
            return (m - 1) * a[d] + p + self.luckyNumber(n % p)
        else:
            return m * a[d] + self.luckyNumber(n % p)
