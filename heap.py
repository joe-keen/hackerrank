class Heap(object):
    def __init__(self):
        self.heap = []
    
    def leftChildIndex(self, index):
        return 2 * index + 1
    def rightChildIndex(self, index):
        return 2 * index + 2
    def parentIndex(self, index):
        return (index - 1) / 2
    
    def hasLeftChild(self, index):
        return index < len(self.heap)
    def hasRightChild(self, index):
        return index < len(self.heap)
    def hasParent(self, index):
        return self.parentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.heap[self.leftChildIndex(index)]
    def rightChild(self, index):
        return self.heap[self.rightChildIndex(index)]
    def parent(self, index):
        return self.heap[self.parentIndex(index)]
    
    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
        
    def peek(self):
        return self.heap[0]
    
    def poll(self):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapifyDown()
        return result
    
    def add(self, item):
        print "add: {}".format(item)
        self.heap.append(item)
        self.heapifyUp()
        
    def heapifyUp(self):
        index = len(self.heap) - 1
        print "heapifyUp: {} | {} | {} | {}".format(index, self.hasParent(index), self.parent(index), self.heap[index])
        # print index
        while (self.hasParent(index) and self.parent(index) > self.heap[index]):
            print "swap: {} | {}".format(self.parentIndex(index), index)
            print "heap before: {}".format(self.heap)
            self.swap(self.parentIndex(index), index)
            print "heap after: {}".format(self.heap)
            index = self.parentIndex(index)
            print "index: {}".format(index)
            
    def heapifyDown(self):
        index = 0
        while (self.hasLeftChild(index)):
            smallestChild = self.leftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallestChild = self.rightChildIndex(index)
            
            if self.heap[index] < self.heap[smallestChild]:
                break
                
            self.swap(index, smallestChild)
            index = smallestChild
