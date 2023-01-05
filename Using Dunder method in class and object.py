class Rhon:
    def __init__(self, name, salary, salary2):
        self.name = name
        self.salary = salary
        self.salary2 = salary2

    def __add__(self, other):
        return self.salary + other.salary
r1 = Rhon("Rohan", 700, 60000)
r2 = Rhon("Mohan", 500, 30000)

print("Name: ", r1.name)
print("Slary: ", r1.salary)
print("Net worth: ", r1.salary2)
print(r1+r2)
# print("Name: ", r2.name)
# print("Slary: ", r2.salary)
# print("Net worth: ", r2.salary2)