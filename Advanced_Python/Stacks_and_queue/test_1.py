

class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def count(self):
        return len(self.values)


s = Stack()

for v in range(5, 10):
    s.push(v)

print(s.pop())
print(s.peek())
print(s.count())