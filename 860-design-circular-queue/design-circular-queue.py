class Node:
    def __init__(self,val,nxt,prev):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularQueue(object):

    def __init__(self, k):
        self.space = k
        self.left = Node(0,None,None)
        self.right = Node(0,None,self.left)
        self.left.next = self.right
        
    def enQueue(self, value):
        if self.space == 0: return False
        curr = Node(value,self.right,self.left)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True

    def deQueue(self):
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True
        

    def Front(self):
        if not self.isEmpty():
            return self.left.next.val
        return -1
        
    def Rear(self):
        if not self.isEmpty():
            return self.right.prev.val
        return -1
        
    def isEmpty(self):
        if self.left.next == self.right:
            return True
        else:
            return False
        
    def isFull(self):
        if self.space == 0:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()