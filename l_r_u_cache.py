"""LRU Cache - Implement Least Recently Used cache."""

# LRU Cache
# Fixed Size: Cache needs to have some bounds to limit memory usages.
# Fast Access: Cache Insert and lookup operation should be fast , preferably O(1) time.
# Replacement of Entry in case , Memory Limit is reached: A cache should
# have efficient algorithm to evict the entry when memory is full.


class LRUCache:
    """LRUCache class."""

    # Node with previous and next pointers
    class Node:
        """Node class."""

        def __init__(self, key, value):
            """__init__ function."""
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    # initialising capacity hashmap head tail and setting pointers of head and
    # tail to each other
    def __init__(self, capacity: int):
        """__init__ function."""
        self.capacity = capacity
        self.hashmap = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """get function."""
        if self.head.key == key:
            return self.head.value
        if key in self.hashmap:
            valueToReturn = self.hashmap[key]
            self.remove(valueToReturn)
            self.add(valueToReturn)
            return valueToReturn.value
        return -1

    def add(self, Node):
        """add function."""
        Node.prev = self.head
        Node.next = self.head.next
        self.head.next = Node
        Node.next.prev = Node

    def remove(self, Node):
        """remove function."""
        Node.prev.next = Node.next
        Node.next.prev = Node.prev

    def put(self, key: int, value: int) -> None:
        """put function."""
        if key in self.hashmap:
            temp = self.hashmap[key]
            temp.value = value
            self.remove(temp)
            self.add(temp)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.tail.prev.key)
                self.remove(self.tail.prev)
            temp = self.Node(key, value)
            self.add(temp)
            self.hashmap[key] = temp


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)te
# param_1 = obj.get(key)
# obj.put(key,value)
