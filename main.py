user = str(input("Hello my name is python and your name is? "))

print("Hello " + user + ", in this program you can convert kilometers into miles.")

while True:

    print("Please enter the amount of kilometers you'd like to convert!")

    km = input("Kilometers: ")

    km = float(km.replace(",", "."))

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        print("Goodbye " + user)





