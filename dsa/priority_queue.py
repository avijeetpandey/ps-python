class MinPriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        self.queue.append((priority, item))

    def extract(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        min_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i
        return self.queue.pop(min_index)[1]

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        min_item = min(self.queue, key=lambda x: x[0])
        return min_item

    def is_empty(self):
        return len(self.queue) == 0


heap = MinPriorityQueue()
heap.insert(1, "low priority")
heap.insert(2, "high priority")
heap.insert(3, "low priority")

print(heap.extract())
print(heap.peek())


'''
Time complexity of the min heap
insert - O(1)
extract - O(n)
peek - O(n)
'''