import random


def main():
    display()




def driver():
    li = ["😊","👍","🐍","💕","😡","🐸"]
    x = random.choice(li)
    for num in range (0,96):
        if num == 0 or (num%9 == 0) and num != 63:
            print(f"[{num}-{x}]",end=" ")
        elif (num%63 == 0):
            print(f"[{num}-{x}]")
        elif ((num+1)%8 == 0):
            print("[",num,"-",random.choice(li),"]",sep="")                   
        else:
            print("[",num,"-",random.choice(li),"]",end=" ",sep="")
    print()
    return x


def display():
    while True:
        input("Welcome to MIND READER")
        input("Please choose any 2 digit number")
        input("Now reverse the digits of chosen number")
        input("Now subtract the smaller number with bigger number")
        input("Memorize the obtained number")
        input("look at the emoji beside the obtained number")
        y = driver()
        input()
        print("Your emoji is : ",y)
        val = input("If you want to continue enter 'Y'\n")
        if val.lower() != "y":
            return False

main()


