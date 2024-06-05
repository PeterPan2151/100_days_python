line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
index_digit = position[0]
row = int(position[1]) - 1

if index_digit == 'A':
    index_digit = 0
elif index_digit == 'B':
    index_digit = 1
elif index_digit == 'C':
    index_digit = 2

map[row][index_digit] = 'X'


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")