import random
while True:
 
   hidden = random.randrange(1, 10)
 
   guess = int(input("Please enter your guess: "))
 
   if guess == hidden:
     print("you are absoutely right")
     print("congratulations")
   elif guess < hidden:
     print("Your guess is too low")
     print(hidden,"this is the lucky number")
   else:
     print("Your guess is too high")
     print(hidden,"this is the lucky number")
