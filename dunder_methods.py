class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)


e = Employee("John")

print(e)       # John
print(len(e))  # 4

# print(e) internally calls e.__str__().
# len(e) internally calls e.__len__().

# Dunder means Double Underscore

#  Method	        Purpose
# __init__()	    Initializes an object
# __str__()	      Defines its readable string representation
# __len__()	      Defines what len() returns
# __eq__()	      Defines ==
# __hash__()	    Defines hashing
# __iter__()	    Makes an object iterable
# __next__()	    Returns the next item
# __add__()	      Defines +
