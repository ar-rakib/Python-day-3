print("welcome to the Roller Coaster")

height = int(input("What is your height in cm? "))

if height>120:
    print("You can ride Roller Coaster!")
    age = int(input("what is your age? "))

    if age<12:
        print("Please pay 5 dollar.")
    elif age<=18:
        print("Please pay 8 dollar")
    else:
        print("Please pay 12 dollar.")

else:
    print("Sorry ! You have to grow taller before riding Roller Coaster!")