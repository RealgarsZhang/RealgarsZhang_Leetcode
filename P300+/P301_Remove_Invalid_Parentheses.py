def helper(s,prog,item,left_num,right_num,res):
    if prog==len(s):       
        res.add(item)
        return
    if s[prog]!=')':
        helper(s,prog+1,item+s[prog],left_num+int(s[prog]=='('),right_num,res)
    else:
        if left_num>right_num:
            helper(s,prog+1,item+s[prog],left_num,right_num+1,res)
        else:
            helper(s,prog+1,item,left_num,right_num,res)
            for i in range(len(item)):
                if item[i] == ')':
                    helper(s,prog+1,item[:i]+item[i+1:]+')',left_num,right_num,res)
def helper_lr(s,prog,item,left_num,right_num,res):
    if prog<0:
        res.add(item)
        return
    if s[prog]!='(':
        helper_lr(s,prog-1,s[prog]+item,left_num,right_num+int(s[prog]==')'),res)
    else:
        if right_num>left_num:
            helper_lr(s,prog-1,'('+item,left_num+1,right_num,res)
        else:
            helper_lr(s,prog-1,item,left_num,right_num,res)
            for i in range(len(item)):
                if item[i] == '(':
                    helper_lr(s,prog-1,'('+item[:i]+item[i+1:],left_num,right_num,res)

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        temp_res = set()
        helper(s,0,'',0,0,temp_res)
        #print temp_res
        res = set()
        for string in temp_res:
            n = len(string)
            helper_lr(string,n-1,'',0,0,res)
            
        return list(res)
  
