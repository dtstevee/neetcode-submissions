class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [None]

        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        self.heap.append(val)

        i = len(self.heap) - 1
        
        while i > 1:
            parent = i // 2

            if self.heap[parent] <= self.heap[i]:
                break
            
            else:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            
            i = parent

        # maintain the min heap, tick out not useful numbers
        if len(self.heap) - 1 > self.k:
            self.pop()
        
        return self.heap[1]
    
    def pop(self):
        if len(self.heap) == 2:
            return self.heap.pop()
        
        minimum = self.heap[1]
        self.heap[1] = self.heap.pop()

        # starting of the sift down process
        i = 1
        
        while 2*i < len(self.heap):
            left = 2*i
            right = 2*i +1

            # assume left is small
            smaller = left
            
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smaller = right
            
            if self.heap[i] <= self.heap[smaller]:
                break

            self.heap[i], self.heap[smaller] = self.heap[smaller], self.heap[i]
            
            i = smaller
            
        



        
