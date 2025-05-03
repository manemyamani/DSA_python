class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # for enqueue
        self.stack2 = []  # for dequeue

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if not self.stack2:
            # Transfer elements only if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("Queue is empty")
            return
        return self.stack2.pop()

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("Queue is empty")
            return
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def display(self):
       for i in  self.stack2:
        print(i)

# Test
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Front:", q.front())
print("Dequeue:", q.dequeue())
q.display()
