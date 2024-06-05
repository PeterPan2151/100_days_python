print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
full_name = (name1 + name2).lower()
t = full_name.count('t')
r = full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')
l = full_name.count('l')
o = full_name.count('o')
v = full_name.count('v')

first_digit = t + r + u + e 
second_digit = l + o + v + e
final_score = int(str(first_digit) + str(second_digit))

if 10 > final_score or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif 40 <= final_score <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")

