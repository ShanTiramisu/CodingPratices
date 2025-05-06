import math

class MaxHeap:
    def __init__(self,capacity):
        #capactity is max elements you to want to store within the heap first
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
    
    def getParentIndex(self, index):
        return (index-1)//2
    
    def getLeftChildIndex(self, index):
        return index*2+1
    
    def getRightChildIndex(self, index):
        return index*2+2
    
    def hasParent(self,index):
        '''
        To check wheather the parent or not
        '''
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
        
    def heapifyUp(self, index):
        if (self.hasParent(index) and self.parent(index) < self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))
    
    def insert(self, data):
        if self.isFull():
            raise("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1) 

    def removeMin(self):
        if self.size == 0:
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data
    
    def heapifyDown(self, index):
        largest = index
        if (self.hasLeftChild(index) and self.storage[largest] < self.leftChild(index)):
            largest = self.getLeftChildIndex(index)
        if (self.hasRightChild(index) and self.storage[largest] < self.rightChild(index)):
            largest = self.getRightChildIndex(index)
        if (largest != index):
            self.swap(index, largest)
            self.heapifyDown(largest)

    def print_heap_tree(self, index, level):
        """Prints a heap as a tree structure."""
        if self.size == 0:
            print("Empty heap")
            return
    
        levels = math.floor(math.log2(self.size)) + 1
        max_width = 2 ** levels * 2  # rough estimate for pretty spacing

        index = 0
        for level in range(levels):
            level_count = 2 ** level
            spacing = max_width // (level_count + 1)

            line = ""
            for i in range(level_count):
                if index >= self.size:
                    break
                line += " " * spacing + str(self.storage[index])
                index += 1
            print(line)

            

if __name__ == "__main__":
    values = [20, 10 , 5, 8, 15, 30, 9,0,1]
    h = MaxHeap(len(values))
    for val in values:
        h.insert(val)
    print(h.storage)
    h.print_heap_tree(0,0)

