#class A:
#    classvar1 = "I am a class variable in class A"
#    def __init__(self):
#        self.var1 = "I am inside class A's constructor"
#        self.classvar1 = "Instance var in class A"
#        self.special = "Special"
#
#class B(A):
#    classvar1 = "I am in class B"
#
#    def __init__(self):
#        self.var1 = "I am inside class B's constructor"
#        self.classvar1 = "Instance var in class B"
#        # super().__init__()
#        # print(super().classvar1)
#
#
#a = A()
#b = B()
#
#print(b.special, b.var1, b.classvar1)

class Asus:
    hacker = 10
    def __init__(self):
        self.emp = 100
        self.worker = 200
        self.value = 8
        self.popu = "Asus Tuf F-15 Gaming Laptop"
        print("Total no of hackers ", self.hacker)

class GitHub(Asus):
    hacker = 30
    def gitcompany(self):
        print(self.hacker)

    def __init__(self):
        super().__init__()
        self.emp = 200
        self.worker = 700
        self.value = 9
a = Asus()
gh = GitHub()
print("Asus emp ", a.emp)
print("Total worker ", a.worker)

#print("Popular laptop ", gh.popu) 
#Give Error
#we use -> super().__init__()