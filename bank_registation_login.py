print("Welcome to the 'Y Bank',")

s = input("[1] Register  or  [2]  Login : ")
#        Register starts from here
if s == "1":
    print()
    print()
    print("Registation")
    print()
    print()
    name = input("Enter Your name : ")
    print()

    print("Hello", name,"," )
    print("Enter a Valid age")
    print("The Age should be 18+ for opening bank")
    print("After 75 years you should Come for KYC.")
    print()

    age = int(input("Please enter your age here : "))
    if age == 0:
        print(name, "You are Entering an Invalid Age '0'. Please Enter a valid Age.")
    elif age <= 18:
        print("You're age is less than 18, Your Age :", age,". If you want to register so come after",18-age, "Years")
    elif age >= 18:
        print("Registation Sucessfull")
        print()
        print("Hello Mr.", name,',')
        print()
        first_balance = int(input("Enter Your Amount for open an Account min = 50(Rupee) : ₹"))
        if first_balance <= 50:
            print("Sorry we doesn't register because you entered the amount is less than 50 Rupees, So go and try again to register. Your Amount is :", first_balance, "You need", 50 - first_balance, "more rupees to Register.")
        else:
            print()
            print("Amount Submitted Sucessful")
            print("Now go and Login...")

#            Login starts from here

elif s == "2":
    print()
    print()
    print("Login")
    print()
    print()
    name = input("Enter Your name : ")
    print()
    print("Welcome back Mr.",name,',')
    print()
    if name == "Yatharth" or name == "YATHARTH" or name == "yatharth":
        total_bal = 500
        Loption = input("[1] Deposite Money [2] Widraw Money [3] Balance Enquiry [4] Go Back : ")
        print()
        if Loption == "1":
            print("Deposite Money...")
            print()
            DM = int(input("Enter Amount to be Deposite : ₹"))
            print()
            print("Money deposited Sucessful, Amount : ₹",DM)
            print()
            print("Total Balance : ₹",total_bal+DM)
        elif Loption == "2":
            print("Widraw Money...")
            print()
            WM = int(input("Enter Amount to be Widraw : ₹"))
            print()
            print("Money Widraw Sucessful, Amount : -₹",WM)
            print()
            print("Total Balance : ₹",total_bal-WM)
        elif Loption == "3":
            print("Balance Enquiry...")
            print()
            print("Total Balance : ₹",total_bal)
        else:
            print("Thanks for Coming...")
    elif name == "Shaurya" or name == "SHAURYA" or name == "shaurya":
        total_bal = 1000
        Loption = input("[1] Deposite Money [2] Widraw Money [3] Balance Enquiry [4] Go Back : ")
        print()
        if Loption == "1":
            print("Deposite Money...")
            print()
            DM = int(input("Enter Amount to be Deposite : ₹"))
            print()
            print("Money deposited Sucessful, Amount : ₹",DM)
            print()
            print("Total Balance : ₹",total_bal+DM)
        elif Loption == "2":
            print("Widraw Money...")
            print()
            WM = int(input("Enter Amount to be Widraw : ₹"))
            print()
            print("Money Widraw Sucessful, Amount : -₹",WM)
            print()
            print("Total Balance : ₹",total_bal-WM)
        elif Loption == "3":
            print("Balance Enquiry...")
            print()
            print("Total Balance : ₹",total_bal)
        else:
            print("Thanks for Coming...")
    else:
        print("User doesn't found...")
