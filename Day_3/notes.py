print("Welcome to my rollercoaster.")
height = int(input("Enter your height in cm: "))

ticket = 0

if height >= 120:
    print("You can ride the rollercaoster")
    age = int(input("What is your age? "))
    if age >= 18:
       ticket += 12
       print(f"Please pay ${ticket}") 
    elif 12 <= age <18:
        ticket += 7
        print(f"Please pay ${ticket}")
    elif age < 12:
        ticket += 5
        print(f"Please pay ${ticket}")

    photo_taken = input("Do you want a photo taken? Y or N? ").lower()
    if photo_taken == 'y':
        ticket += 3
    print(f"Please pay ${ticket}")
else:
    print("Sorry, you cant ride.")