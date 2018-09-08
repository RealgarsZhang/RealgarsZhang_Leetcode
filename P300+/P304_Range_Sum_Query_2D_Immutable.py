class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        if n==0:
            return
        
        m = len(matrix[0])
        if m==0:
            return
        self.cum_sum = []
        self.cum_sum.append([0]*(m+1))
        
        for i in range(n):
            row_sum = [0]*(m+1)
            for j in range(m):
                row_sum[j+1] = row_sum[j]+matrix[i][j]
            for j in range(m):
                row_sum[j+1] += self.cum_sum[-1][j+1]
            self.cum_sum.append(row_sum)
        ''' 
        for l in self.cum_sum:
            print l
        for l in matrix:
            print l
        '''

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        return self.cum_sum[row2+1][col2+1]-self.cum_sum[row1][col2+1]-self.cum_sum[row2+1][col1]+self.cum_sum[row1][col1]
        


