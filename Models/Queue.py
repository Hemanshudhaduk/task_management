from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self,item):
        # item = input("Enter the item to enqueue: ")
        self.items.append(item)
        # print(f"Enqueued: {item}")

    def dequeue(self):
            item = self.items.popleft()
            # print(f"Dequeued: {item}")
            return item
    
    def is_empty(self):
        return len(self.items) == 0