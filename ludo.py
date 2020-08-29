import random
while True:
    key=print("Roll the dice by pressing enter")
    print(" ------")
    print("| * * *|")
    print("| * * *|")
    print(" ------")
    input()
    roll=random.randint(1,6)
    print(roll)
    if(roll==1):
     print(" -----")
     print("|     |")
     print("|  *  |")
     print("|     |")
     print(" -----")
    if(roll==2):
     print(" -----")
     print("|     |")
     print("| * * |")
     print("|     |")
     print(" -----")
    if(roll==3):
     print(" -------")
     print("|        |")
     print("| * *  * |")
     print("|        | ")
     print(" --------")
    if(roll==4):
     print(" -----")
     print("| * *  |")
     print("| * *  |")
     print(" -----")
    if(roll==5):
     print(" ------")
     print("|  **   |")
     print("| * * * | ")
     print(" ------")
    if(roll==6):
     print(" ------")
     print("| * * * |")
     print("|* * *  |")
     print(" ------ ")



