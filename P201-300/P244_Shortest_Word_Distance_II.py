class WordDistance(object):
    
    cache_dic = {}
    pos_dic = {}
    n = 0
    def __init__(self, words):
        """
        :type words: List[str]
        """
        
        n = len(words)
        self.n = n
        for i in range(n):
            self.pos_dic.setdefault(words[i],[])
            self.pos_dic[words[i]].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        temp = [word1,word2]
        temp.sort()
        temp = tuple(temp)
        if temp in self.cache_dic:
            return self.cache_dic[temp]
        
        list1 = self.pos_dic[word1]
        list2 = self.pos_dic[word2]
        if list1[-1]<list2[0]:
            res = list2[0]-list1[-1]
        elif list2[-1]<list1[0]:
            res = list1[0] - list2[-1]
        else:
            merged_list = []
            p1 = 0
            p2 = 0
            n1 = len(list1)
            n2 = len(list2)
            while p1<n1 and p2<n2:
                if list1[p1]<list2[p2]:
                    merged_list.append((list1[p1],1))
                    p1 += 1
                else:
                    merged_list.append((list2[p2],2))
                    p2 += 1
            while p1<n1:
                merged_list.append((list1[p1],1))
                p1 += 1
            while p2<n2:
                merged_list.append((list2[p2],2))
                p2 += 1
            res = self.n+1
            for i in range(len(merged_list)-1):
                if merged_list[i][1]!=merged_list[i+1][1]:
                    res = min(res,merged_list[i+1][0]-merged_list[i][0])
        
        self.cache_dic[temp] = res
        return res
        


