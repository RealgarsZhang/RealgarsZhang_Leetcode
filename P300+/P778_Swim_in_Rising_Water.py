def dfs(num,i,j,grid,visited):
    N = len(grid)
    if i==N-1 and j==N-1:
        return True
    visited.add((i,j))
    reachable = False
    if i>0 and (i-1,j) not in visited and num>=grid[i-1][j]:
        res = dfs(num,i-1,j,grid,visited)  
        reachable = reachable or res
    if not reachable and j>0 and (i,j-1) not in visited and num>=grid[i][j-1]:
        res = dfs(num,i,j-1,grid,visited)     
        reachable = reachable or res

    if not reachable and i<N-1 and (i+1,j) not in visited and num>=grid[i+1][j]:
        res = dfs(num,i+1,j,grid,visited)       
        reachable = reachable or res
        
    if not reachable and j<N-1 and (i,j+1) not in visited and num>=grid[i][j+1]:
        res = dfs(num,i,j+1,grid,visited)  
        reachable = reachable or res
    
    
    return reachable
      
    

def canReach(num,grid):
    if num<grid[0][0]:
        return False
    visited = set()
    return dfs(num,0,0,grid,visited)

    
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        l = 0
        r = N*N-1
        while l<r:
            mid = (l+r)/2
            if canReach(mid,grid):
                r = mid
            else:
                l = mid + 1
        
        return r
        
