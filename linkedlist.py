"""Linked List - Implement singly linked list operations."""


class Node:
    """Node class."""

    def __init__(self, val):
        """__init__ function."""
        self.val = val
        self.next = None

    def __repr__(self):
        """__repr__ function."""
        return "Node data is = {}".format(self.val)

    def getval(self):
        """getval function."""
        return self.val

    def setval(self, new_val):
        """Replace the data with new"""
        self.val = new_val

    def getnext(self):
        """ "Return next attribute"""
        return self.next

    def setnext(self, new_next):
        """ "new next"""
        self.next = new_next


class SinglyLinkedList:
    """SinglyLinkedList class."""

    def __init__(self):
        """__init__ function."""
        self.head = None
        # self.length = 0

    def __repr__(self):
        """__repr__ function."""
        return "SLL object: head={}".format(self.head)

    def is_empty(self):
        """returns true if linked list is empty"""
        return self.head is None

    def add_front(self, val):
        """add_front function."""
        temp = Node(val)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        """size function."""
        size = 0
        if self.head is None:
            return size
        current = self.head
        while current:  # while there are nodes to count
            size += 1
            # current = current.next
            current = current.getnext()
        return size

    def search(self, searchterm):
        """search function."""
        if self.head is None:
            return "Linked list is empty, no nodes to search"
        current = self.head
        while current:
            if current.getval() == searchterm:
                return True
            else:
                current = current.getnext()
        return False

    def remove(self, val):
        """remove function."""
        if self.is_empty():
            return "List is empty, nothing to remove"
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getval() == val:
                found = True
            else:
                if current.getnext() is None:
                    return "Node not found"
                else:
                    previous = current
                    current = current.getnext()
        if previous is None:
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
    print(sll.is_empty())
    sll.head = node1
    print(sll.is_empty())
    sll.add_front("Barry")
    print(sll.head)
    print(sll.size())
    print(sll.search("barry"))
