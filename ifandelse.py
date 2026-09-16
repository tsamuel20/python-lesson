# phone number, amount, pincode,
# validation, pincode check, check balance,

print("welcome to momo services")

balance = 10000
pincode = "1234"

print("MTN mobile money")
print("1. send mobile money")
print("2. buy airtime")
print("3. check balance")

option = input("select an option ")

if option == "1":
    phone = input("ener recipient phone number ")
    amount = int(input("enter amount to send "))
    pin = input("enter your 4 digit pincode ")

    if pin != pincode:
        print("invalid pin")
    else:
        if amount > balance:
            print ("insuficient balance")
        else:
            if amount <= 0:
                print("enter amount above zero")
            else:
                balance = balance - amount
                print("transacttion soccessful")
                print(f"you have sent {amount} to {phone}")
                print(f"your balance left is {balance}")


elif option == "2":
    print("1. self")
    print("2. others")
    airtime_choice = input("select your choice")

    amount = int(input("enter amount to buy "))
    pin = input("enter your 4 digit pincode ") 

    if pin != pincode:
        print("invalid pin")
    else:
        if amount > balance:
            print ("insuficient balance")
        else:
            if amount <= 0:
                print("enter amount above zero")
            else:
                balance = balance - amount
                print("transacttion successful")
                print("you have successfully buy an airtime of {amount} for your self")
                print(f"your balance left is {balance}")

                # if airtime_choice == 2:
                #      phone = input("ener recipient phone number ")
                #      amount = int(input("enter amount to buy "))
                #      pin = input("enter your 4 digit pincode ")
                     
                #      if pin != pincode:
                #              print("invalid pin")
                #      else:
                #          if amount > balance:
                #              print ("insuficient balance")
                #          else:
                #              if amount <= 0:
                #                  print("enter amount above zero")
                #              else:
                #                  balance = balance - amount
                #                  print("transacttion soccessful")
                #                  print("you have successfully buy an airtime of {amount} to {phone}")
                #                  print(f"your balance left is {balance}")


elif option == "3":
    pin = input("enter your 4 digit pincode ")
    if pin == pincode:
        print(f"you have GHC {balance} in your mobile money wallet")
    else:
        print("invalid pin")
else:
    print("invalid or unknown option")
                     
                                     
                     
