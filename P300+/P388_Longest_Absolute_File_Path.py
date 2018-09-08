class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        parsed_input = input.split('\n')
        
        
        stack = []
        temp_val = 0
        max_val = 0
        for name in parsed_input:
            name_list = name.split('\t')
            
            level = len(name_list)
            if not stack:
                stack.append( (name_list[-1],level) )
                temp_val += len(name_list[-1])
                
            elif level>stack[-1][1]:
                stack.append( (name_list[-1],level) )
                temp_val += len(name_list[-1]) +1
            else:
                if len(stack[-1][0].split('.'))>1:    
                    max_val = max(max_val,temp_val)
                while stack and level<=stack[-1][1]:
                    temp_val -= (len(stack[-1][0])+1)
                    stack.pop()
                if not stack:
                    temp_val = len(name_list[-1])
                else:
                    temp_val += len(name_list[-1]) + 1
                stack.append( (name_list[-1],level) )
        
        if stack and len(stack[-1][0].split('.'))>1:
            max_val = max(max_val,temp_val)
        return max_val
  
