class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        n = len(secret)
        s_dic = {}
        g_dic = {}
        for i in range(n):
            if secret[i]==guess[i]:
                bull+=1
            else:
                s_dic.setdefault(secret[i],0)
                g_dic.setdefault(guess[i],0)
                s_dic[secret[i]] += 1
                g_dic[guess[i]] += 1
        
        for key in s_dic:
            if key in g_dic:
                cow+=min(s_dic[key],g_dic[key])
                
        return str(bull)+'A'+str(cow)+'B'
  
