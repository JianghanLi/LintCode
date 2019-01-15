class Solution:
    """
    @param s: the English word
    @return: The number of keystrokes
    """
    def getAns(self, s):
        # Write your code here
        isupper = []
        for c in s:
            if c.isupper():
                isupper.append(1)
            else:
                isupper.append(0)

        status = 0
        stroke = 0

        for i in range(len(s)):
            if isupper[i] == status:
                stroke += 1
            else:
                if i < len(s) - 1 and isupper[i] == isupper[i + 1]:
                    # press caps lock
                    status = 1 - status
                    stroke += 2
                else:
                    # press shift
                    stroke += 2

        return stroke
