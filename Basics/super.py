# super() is used in inheritance to access methods from the parent class.

class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class Manager(Employee):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team


m = Manager("John", "Cloud")
m.display()
