# - return → Returns a value and ends the function.
# - yield → Returns a value and pauses the function, remembering where it stopped.
  
def normal():
    return 10
    return 20

print(normal())  # 10


#yield

def numbers():
    yield 10
    yield 20
    yield 30

for n in numbers():
    print(n)

# Output: 10 20 30

# They produce values one at a time instead of storing all values in memory.

# Practical example – reading a large log file:

def read_errors(file):
    with open(file) as f:
        for line in f:
            if "ERROR" in line:
                yield line

# We use generators with yield to process large files lazily.
# Instead of collecting all matching records in a list, we return one matching line at a time. This reduces memory consumption, especially when processing large log files
