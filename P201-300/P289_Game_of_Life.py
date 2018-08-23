def helper(board,row,col):
    m = len(board)
    n = len(board[0])
    num_alive_neigh = 0
    if row>0 and board[row-1][col]/2 >0:
        num_alive_neigh += 1
    if col>0 and board[row][col-1]/2 >0:
        num_alive_neigh += 1
    if col<n-1 and board[row][col+1] == 1:
        num_alive_neigh += 1
    if row<m-1 and board[row+1][col] == 1:
        num_alive_neigh += 1
    if row<m-1 and col<n-1 and board[row+1][col+1]==1:
        num_alive_neigh += 1
    if row<m-1 and col>0   and board[row+1][col-1]==1:
        num_alive_neigh += 1
    if row>0   and col<n-1 and board[row-1][col+1]/2>0:
        num_alive_neigh += 1
    if row>0   and col>0   and board[row-1][col-1]/2>0:
        num_alive_neigh += 1
    if board[row][col] ==0:
        board[row][col] =  (num_alive_neigh==3)
    else:
        board[row][col] = 2+ (num_alive_neigh==2 or num_alive_neigh ==3)



class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #Encode the changes and finalize the changes when no longer needed.
        #00:die->die 01:die->alive, similar things follow
        m = len(board)
        
        if m==0:
            return board
        n= len(board[0])
        for i in range(m):
            for j in range(n):
                helper(board,i,j)
        
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
        
   
