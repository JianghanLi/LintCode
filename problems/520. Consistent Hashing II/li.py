import random
class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """

    @classmethod
    def create(cls, n, k):
    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
        self = cls()
        self.k = k
        self.n = n
        self.pool = range(n)
        random.shuffle(self.pool)
        self.machine = {}
        return self

    def addMachine(self, machine_id):
        """
        @param: hashcode: An integer
        @return: A machine id
        """
        res = [self.pool.pop() for i in range(self.k)]
        for m in res:
            self.machine[m] = machine_id
        return res

    def getMachineIdByHashCode(self, hashcode):
        m = min([m for m in self.machine], key=lambda m: (m + self.n - hashcode) % self.n)
        return self.machine[m]
