from collections import deque

q = deque()
# Enqueue , push, add
q.append(2)    # appendRight()
q.append(3)    # appendRight()
# q.appendleft(3)

print(q)
# Dequeue, pop, remove
# q.pop()    # popRight()
q.popleft()

print(q)

# Peek
print(q[0])

# Count
print(len(q))