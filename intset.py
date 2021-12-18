class IntSet(object):
"""
IntSet is a set of int.
"""
#  this is about implent not about interface 
#  
#
    def __init__(self):
    """ create an empty intset """
        self.vals = []
    
    def insert(self, e):
    """ if e is an int, insert e"""
        self.vals.append(e)

    def member(self, e):
    """ if e is int
        if e in self, return True, else raise ValueError"""
	    try:
		self.vals.remove(e)
	    except:
		raise ValueError(str(e) + ' not fond')
           
    def remove
   
