class Node(object):
    def __init__(self,input):
        self.string = input
        self.adj_list = []# stores [adj_node,quotient]
        self.value = []# stores [root,quotient],dfs works for it.

class Solution(object):
    def dfs(self,node,root,coeff):
        node.value = [root,coeff]
        for item in node.adj_list:
            if item[0].value==[]:
                self.dfs(item[0],root,coeff/item[1])
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        n = len(equations)
        zeros =set()
        node_dict = {}# str->node
        for i in range(n):
            eqn = equations[i]
            val = values[i]
            if val == 0.0:
                zeros.add(eqn[0])
            else:
                if eqn[0] not in node_dict:
                    node_dict[eqn[0]] = Node(eqn[0])
                if eqn[1] not in node_dict:
                    node_dict[eqn[1]] = Node(eqn[1])
                node_dict[eqn[0]].adj_list.append([node_dict[eqn[1]],val])
                node_dict[eqn[1]].adj_list.append([node_dict[eqn[0]],1.0/val])
        
        for key in node_dict:
            if node_dict[key].value==[]:
                self.dfs(node_dict[key],node_dict[key],1.0)
        res = []
        for query in queries:
            if query[0] in zeros:
                res.append(0.0)
            elif query[0] not in node_dict \
            or query[1] not in node_dict\
            or node_dict[query[0]].value[0] != node_dict[query[1]].value[0]:
                res.append(-1.0)
            else:
                res.append(node_dict[query[0]].value[1]/node_dict[query[1]].value[1])
                
        return res
   
