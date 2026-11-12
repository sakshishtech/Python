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

# Iterable: An object you can loop over.
# Iterator: An object that gives you one value at a time using next().
