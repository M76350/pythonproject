#
import random
user=int(input("enter a number mainually---------------"))
computer_number=random.randrange(1,101)

if user>computer_number:
  print("computer random number",computer_number)
  print("your gess number is too high")
elif computer_number>user:
  print("computer random number",computer_number)
  print("your guess is too low")
else:
  print("computer random number",computer_number)
  print("your guess number is equeal to be  computer number")
  