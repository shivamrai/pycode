class Node:
    def __init__(self,val):
        self.val = val
        self.next  = None
    
    def __repr__(self):
        return "Node data is = {}".format(self.val)

    def getval(self):
        return self.val

    def setval(self, new_val):
        """Replace the data with new"""
        self.val = new_val

    def getnext(self):
        """"Return next attribute"""
        return self.next

    def setnext(self,new_next):
        """"new next"""
        self.next = new_next

if __name__ == "__main__":
    node = Node('apple')
    node.getval()
    node.setval(7)
    node.getval()
    node2  = Node('carrot')
    node.setnext(node2)
    print(node.getnext())