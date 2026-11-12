class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary


e1 = Employee(50000)
e2 = Employee(60000)

print(e1 + e2)  # 110000

print(e1.__add__(e2))

# Operator overloading means giving standard operators (+, -, *, etc.) custom behavior for user-defined objects.
