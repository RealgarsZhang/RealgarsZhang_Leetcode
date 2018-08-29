class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1!=word2:
            list1 = []
            list2 = []
            for i in range(len(words)):
                if words[i] == word1:
                    list1.append(i)
                elif words[i] == word2:
                    list2.append(i)
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
                res = len(words)+1
                for i in range(len(merged_list)-1):
                    if merged_list[i][1]!=merged_list[i+1][1]:
                        res = min(res,merged_list[i+1][0]-merged_list[i][0])
        else:
            list1 = []
            for i in range(len(words)):
                if words[i] == word1:
                    list1.append(i)
            res = len(words) + 1       
            for i in range(len(list1)-1):
                res = min(res,list1[i+1]-list1[i])
        
        return res
            
 
