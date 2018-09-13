class Solution(object):
    
    def find(self,num,parent):
        if parent[num] == num:
            return num
        parent[num] = self.find(parent[num],parent)
        return parent[num]
    
    def union(self,num1,num2,parent,rank):
        class1 = self.find(num1,parent)
        class2 = self.find(num2,parent)
        if rank[class1]>rank[class2]:
            parent[class2] = class1
        elif rank[class1]<rank[class2]:
            parent[class1] = class2
        else:
            parent[class2] = class1
            rank[class1] += 1
        
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = range(n)
        rank = [0]*n
        if len(edges)!=n-1:
            return False
        for edge in edges:
            if self.find(edge[0],parent) != self.find(edge[1],parent):
                self.union(edge[0],edge[1],parent,rank)
            else:
                return False
        
        return True
