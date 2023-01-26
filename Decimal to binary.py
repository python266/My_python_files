
def binary_search():
    global x, y
    i = int(input("ENTER NUMBER: "))
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
         print(f"Your result is: ", bin(i)[2:])
binary_search()

#x = x%2 = y
#y = y%2 = z
#z = z%2 = a
#.....