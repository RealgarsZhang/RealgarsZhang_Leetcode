def gcd(m,n):
    while m%n!=0:
        m,n = n,m%n
    return n

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return z==0 or (x+y>=z and z%gcd(x,y)==0)
#It is interesting to see how to show the problem is isomorphic to a Diophantineproblem.
#Use induction. Let's assume at a step, the water in either jug is a linear combination of x and y. 
#Any operation will lead to linear combination amount of water in either jug.         
