from collections import deque
q=deque()
for i in range(5):
    q.append(int(input("enter items")))
print(q.popleft())
print(len(q))
print(list(q))


   




