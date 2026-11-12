
class Employee:
    company = "Microsoft"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show_name(self):
        return self.name

    # Class method, when you need to access class level data  for eg company common variable
    @classmethod
    def show_company(cls):
        return cls.company

    # Static method, this doesn't uses self
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0


e1 = Employee("John")

print(e1.show_name())                  # John
print(Employee.show_company())        # Microsoft
print(Employee.is_valid_name("John")) # True
