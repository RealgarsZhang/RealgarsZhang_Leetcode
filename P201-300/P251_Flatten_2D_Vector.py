class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d =[]
        for l in vec2d:
            if l:
                self.vec2d.append(l)
        self.pos = [0,0]
        self.touchend = len(self.vec2d)==0

    def next(self):
        """
        :rtype: int
        """
        res = self.vec2d[self.pos[0]][self.pos[1]]
        if len(self.vec2d[self.pos[0]])-1 == self.pos[1]:
            if self.pos[0] < len(self.vec2d)-1:
                self.pos[0] += 1
                self.pos[1] = 0
            else:
                self.touchend = True
        else:
            self.pos[1] += 1
                
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.touchend
            
        
