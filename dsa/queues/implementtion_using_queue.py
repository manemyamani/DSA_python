from queue import Queue
q=Queue()
for i in range(5):
    q.put(int(input("enter items")))
print(q.get())
print(q.empty())
print(q.qsize())
print(q.task_done()) # it marks the task done or not