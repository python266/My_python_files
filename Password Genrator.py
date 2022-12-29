import string
import random

s1= string.ascii_lowercase
s2= string.ascii_uppercase
s3= string.digits
s4= string.punctuation

user = int(input("Enter your length of your password: "))

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print("".join(random.sample(s, user)))