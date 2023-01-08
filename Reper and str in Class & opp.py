class Happy:
    def __repr__(self):
        return  "Hello I in class Happy"

    def __str__(self):
        i = input("Enter your name: ")
        return f"Hello! Your name is {i}."

h1 = Happy()
print(h1.__repr__())
print(h1.__str__())