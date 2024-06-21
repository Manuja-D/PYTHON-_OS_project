print("WELCOME TO THE NOTE APP \n")
i = input("Enter a Note to take down : ")

print(i)

permenent_note = "n"

y_or_n = input("do you need to save this file? (y or n) :")

if(y_or_n == "y" or y_or_n == "Y"):
    print(i)
    permenent_note = i

else:
    print("this msg will be deleted after you turn off the machine \n")
    print(i)

print(permenent_note)