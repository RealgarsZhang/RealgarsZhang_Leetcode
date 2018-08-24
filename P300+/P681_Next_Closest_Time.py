def get_next_num(ordered_nums,num):
    pos = ordered_nums.index(num) + 1
    while pos<4:
        if ordered_nums[pos] != num:
            return ordered_nums[pos]
        pos += 1
        
        

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = [0,0,0,0]
        nums[0] = int(time[0])
        nums[1] = int(time[1])
        nums[2] = int(time[3])
        nums[3] = int(time[4])
        
        ordered_nums = nums[:]
        ordered_nums.sort()
        
        #for last digit
        
        if nums[3]<ordered_nums[-1]:
            return time[:4]+str(get_next_num(ordered_nums,nums[3]))
        else:
            nums[3] = ordered_nums[0]
            
        #second last digit
        if nums[2]<ordered_nums[-1]:
            next_num = get_next_num(ordered_nums,nums[2])
            if next_num<=5:
                nums[2] = next_num
                return str(nums[0])+str(nums[1])+":" +str(nums[2])+str(nums[3])
        
        nums[2] = ordered_nums[0]
        
        #first two digits
        if nums[0]==0 or nums[0]==1:
            if nums[1]<ordered_nums[-1]:
                nums[1] = get_next_num(ordered_nums,nums[1])
            else:
                nums[1] = ordered_nums[0]
                if (nums[0]+1)%3 in ordered_nums:
                    nums[0] = (nums[0] + 1)%3
                elif (nums[0]+2)%3 in ordered_nums:
                    nums[0] = (nums[0] + 2)%3
                    
            return str(nums[0])+str(nums[1])+":" +str(nums[2])+str(nums[3])
        else:
            if nums[1]<ordered_nums[-1] and get_next_num(ordered_nums,nums[1])<4:
                nums[1] = get_next_num(ordered_nums,nums[1])
            else:
                nums[1] =ordered_nums[0]
                if 0 in ordered_nums:
                    nums[0] = 0
                elif 1 in ordered_nums:
                    nums[0] = 1
                else:
                    nums[0] = 2
            return str(nums[0])+str(nums[1])+":" +str(nums[2])+str(nums[3])
            
     
