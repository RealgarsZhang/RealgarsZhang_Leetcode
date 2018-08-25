class TwoSum(object):
    #add():O(n) find():O(1)
    ''' 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.sums = set()
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        for num in self.nums:
            self.sums.add(num+number)
        self.nums.append(number)
        
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        return value in self.sums
        
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.dict.setdefault(number,0)
        self.dict[number]+=1
        
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.dict:
            if (value-key==key and self.dict[key]>=2) or (value-key!=key and value-key in self.dict):
                return True
            
        return False
            


