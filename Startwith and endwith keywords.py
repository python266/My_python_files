#use of startwith() and endwith() function
#startwith
string = "I am a good boy and I am a programmer"
if string.startswith("Hi"):
    print(True)
else:
    print(False)
#endswith method
if string.endswith("programmer"):
    print(True)
else:
    print(False)
#basic program on the basic of sartswith and endswith keywords
phone = input("Enter your phone number: ")
if phone.startswith("91+"):
    print("Phone number is verified")
else:
    print("Sorry your phone number is belong to India")