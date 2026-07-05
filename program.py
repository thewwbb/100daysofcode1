

height = int(input("Enter hight: "))

if not height > 120:
    print("You are short.   Sorry you can't ride.")
else:
    age = int(input("Enter age: "))

    if age < 12:
        bill = 5
        photos_inqury = input("Do you want photos?")

    elif age > 12 and age < 18:
        bill = 7
        photos_inqury = input("Do you want photos?")
        if photos_inqury == "no":
            print("The bill is $7")
        elif photos_inqury == "yes":
            print("The bill is $10")
        else:
            print("Please enter valid input.")


    elif age >= 18 and age < 45:
        bill = 12
        photos_inqury = input("Do you want photos?")
        if photos_inqury == "no":
            print("The bill is $12")
        elif photos_inqury == "yes":
            print("The bill is $15")
        else:
            print("Please enter valid input.")



    elif age > 45 and age < 55:
        bill = 0
        photos_inqury = input("Do you want photos?")
        if photos_inqury == "no":
            print("The bill is $0")
        elif photos_inqury == "yes":
            print("The bill is $3")
        else:
            print("Please enter valid input.")



    else:
        print("Sorry you can't ride.")
