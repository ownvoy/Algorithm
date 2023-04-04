class Solution(object):
    def __init__(self):
        
        self.hashdict = {}
        self.hashdict[0] = 1
        self.hashdict[1] = 1
        self.hashdict[2] = 2

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.hashdict:
            return self.hashdict[n]

        nlist = [i for i in range(0,n)]
        nlistReverse = list(reversed(nlist))

        for n1 , n2 in zip(nlist, nlistReverse):
            left = self.numTrees(n1)
            right = self.numTrees(n2)
            self.hashdict[n] = self.hashdict.get(n,0)+left*right

        return self.hashdict[n]
