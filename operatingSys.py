def cal():
    on_off = input("enter T to turn on")
    while(on_off == "t" or on_off == "T"):        
        a = int(input("enter a number(pls enter the large number frist) : "))
        b = int(input("enter a number : "))
        opt = input("+ or - or * or / : ")
        on_off = input("is that all (T or F):")

        ans = 0
        
        if(opt == "+"):
            ans = a + b
        elif(opt == "-"):
            ans = a - b
        elif(opt == "*"):
            ans = a * b
        elif(opt == "/"):
            ans = a / b
        else:
            print("Error 404")

        print(ans)

print("Hello there what do you want to do today? ")
print("do you want to open the calculator app ?")

open = input("Y or N  : \n")

if (open == "y" or open == "Y"):
    cal()
elif(open == "n" or open == "N"):

    print("oh well then...nothing to see here for now good luck.")
else:
    
    print("thats not an valid answer for my question...")

