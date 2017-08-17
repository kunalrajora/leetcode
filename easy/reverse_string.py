class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            ne=int(str(x)[1:][::-1])*(-1)
            return ne if ne < (2**31) and ne > (-2**31)  else 0
        else:
	    ne=int(str(x)[::-1])
            return ne if ne <(2**31) and ne > (-2**31)) else 0


