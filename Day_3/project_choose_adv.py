print("Welcome to the treasure island.")
print("Your mission is to find the treasure")
cross_path = input("You're at a cross road. Where do you want to go? Type 'right' or 'left' ").lower()
if cross_path == 'left':
    print("You come to a lake. There is an island in the middle of the lake.")
    lake_choice = input("Type 'wait' to wait for a boat or type 'swim' to swim across. ").lower()

    if lake_choice == 'wait':
        print("You arrive ath the island unharmed. There is a house with 3 doors.")
        door_choice = input("One red, one yellow, and one blue. which color do you choose: ").lower()

        if door_choice == 'blue':
            print("Behind this door is a chest, you open it... \nIt is filled with gold and gems!! Congratulations. You've found the treasure.")
        elif door_choice == 'red':
            print("Behind this door is a chest, you open it... \nThe rooms starts tu burst in flames. Mmm toasty. YOU LOOSE.")
        elif door_choice == 'yellow':
            print("Behind this door is a chest, you open it... \nA lion jumps out, and he looks hungry, luckily, you are the perfect snack. YOU LOOSE.")

    elif lake_choice == 'swim':
        print("You get in the water and starts swimming. But you notice somethings wrong.\nYou get fatigued and cant move. You start drowning and can't breathe anymore. The water cas cursed. YOU LOOSE.")

elif cross_path == 'right':
    print("You were running for quite a while. Then, you don't feel the floor anymore. You fell off a cliff. YOU LOOSE.")