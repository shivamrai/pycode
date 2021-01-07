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

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        #self.length = 0
    
    def __repr__(self):
        return "SLL object: head={}".format(self.head)

    def isEmpty(self):
        """returns true if linked list is empty"""
        return self.head is None

    def addFront(self,val):
        temp = Node(val)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        size = 0
        if self.head is None:
            return size
        current = self.head
        while(current): #while there are nodes to count
            size += 1
            #current = current.next
            current= current.getnext()
        return size

    def search(self,searchterm):
        if self.head is None:
            return "Linked list is empty, no nodes to search"
        current = self.head
        while(current):
            if(current.getval()==searchterm):
                return True
            else:
                current = current.getnext()
        return False


    def remove(self,val):
        if self.isEmpty():
            return "List is empty, nothing to remove"
        current =  self.head
        previous = None
        found = False
        while(not found):
            if(current.getval()==val):
                found = True
            else:
                if(current.getnext()==None):
                    return "Node not found"
                else:
                    previous  = current
                    current = current.getnext()
        if(previous is None):
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())
        return found


if __name__ == "__main__":
    # node = Node('apple')
    # node.getval()
    # node.setval(7)
    # node.getval()
    # node2  = Node('carrot')
    # node.setnext(node2)
    # print(node.getnext())
    node1 = Node(4)
    sll = SinglyLinkedList()
    print(sll.isEmpty())
    sll.head = node1
    print(sll.isEmpty())
    sll.addFront('Barry')
    print(sll.head)
    print(sll.size())
    print(sll.search('barry'))