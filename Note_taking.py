print("WELCOME TO THE NOTE APP \n")
i = input("Enter a Note to take down : ")

print(i)

permenent_note = "n"

y_or_n = input("do you need to save this file? (y or n) :")

if(y_or_n == "y" or y_or_n == "Y"):
    print(i)
    permenent_note = i
    print("Youre note has been added to permentent note")

else:
    print("this msg will be deleted after you turn off the machine \n")
    print(i)

print("We have your permenent notes collected do you want to see them?")
print("(Y OR N)")

ans = input()

if (ans == "y" or ans == "Y"):
    print(permenent_note)
else:
    print("Nothing is saved :} ")