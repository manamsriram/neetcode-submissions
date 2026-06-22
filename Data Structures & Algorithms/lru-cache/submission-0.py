class Node:
    def __init__(self, key: int, val: int):
        self.key ,self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # stores keys, tha point to the nodes in the doubly-linkedlist
        self.Left, self.Right = Node(0,0), Node(0,0) # dummy left and right edge nodes
        self.Left.next, self.Right.prev = self.Right, self.Left
    
    # insert in the right, that is between the Right node and the head. Insert is always the most recently accessed
    def insert(self, node):
        left = self.Right.prev
        self.Right.prev, node.next = node, self.Right
        left.next, node.prev = node, left

    # remove from anywhere in the middle
    def remove(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # remove and move it to the end (MRU position)
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # move to the MRU position
        mru = Node(key, value)
        self.insert(mru)
        self.cache[key] = mru

        if len(self.cache) > self.capacity: # check capacity after put
                lru = self.Left.next
                self.remove(lru)
                del self.cache[lru.key]