class sequence_repeat:
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.count:
            raise StopIteration
        result = self.sequence[self.i % len(self.sequence)]
        self.i += 1
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
