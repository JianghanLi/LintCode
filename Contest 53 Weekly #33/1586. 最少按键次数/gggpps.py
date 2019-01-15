class Solution:
    """
    @param s: the English word
    @return: The number of keystrokes
    """
    def getAns(self, s):
        lock = 1
        not_lock = 0
        for c in s:
            if c >= 'a':  # lowercase
                lock, not_lock = min(lock + 2, not_lock + 2), min(not_lock + 1, lock + 2)
            else:  # uppercase
                lock, not_lock = min(lock + 1, not_lock + 2), min(not_lock + 2, lock + 2)
        return min(lock, not_lock)
