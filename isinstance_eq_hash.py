class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.emp_id == other.emp_id
        return False

    def __hash__(self):
        return hash(self.emp_id)


class Manager(Employee):  # Inheritance
    pass


e1 = Employee(101)
e2 = Employee(101)
m1 = Manager(101)

print(isinstance(m1, Employee))  # True
print(e1 == e2)                  # True
print(hash(e1))                  # Hash value

employees = {e1: "John"}
employees[e2] = "David"

print(employees)  # One key: e1 and e2 are equal
