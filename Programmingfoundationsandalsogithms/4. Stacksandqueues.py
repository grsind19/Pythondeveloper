# Statck - Push, pop
# Queue - Add, remove

#stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)


x = stack.pop()

print(x)


# Queue
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

x = queue.popleft()

print(x)
print(queue)