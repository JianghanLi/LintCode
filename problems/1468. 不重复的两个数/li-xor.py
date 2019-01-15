class Solution:

    def theTwoNumbers(self, a):
        x = x2 = 0
        for i in a: x ^= i
        lowbit = x & -x
        for i in a:
            if lowbit & i:
                x1 ^= i
        return [x2, x ^ x2]
