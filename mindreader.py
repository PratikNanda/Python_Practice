import random
global val
def driver():
    li = ["😊","👍","🐍","💕","😡","🐸"]
    x = random.choice(li)
    for num in range (1,105):
        if (num%72 ==0):
            print("[",num,"-",x,"]")
        elif (num%8 == 0):
            print("[",num,"-",random.choice(li),"]")
        elif (num%9 ==0):
            print("[",num,"-",x,"]",end=" ")                    
        else:
            print("[",num,"-",random.choice(li),"]",end=" ")
    print()
    return x
val = None
while(val == "y"):
    input("Welcome to MIND READER")
    input("Please choose distinct digits 2 digit number")
    input("Now reverse the digits of chosen number")
    input("Now subtract the smaller number with bigger number")
    input("Memorize the obtained number")
    input("look at the emoji beside the obtained number")
    y = driver()
    input()
    print("Your emoji is : ",y)
    val = input("If you want to continue press y\n")
    


