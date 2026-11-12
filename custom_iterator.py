class Count:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.limit:
            raise StopIteration

        self.num += 1
        return self.num


c = Count(3)

for x in c:
    print(x)

# Output: 1 2 3
