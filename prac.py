from time import sleep

def animation(x):
    if x == "circle":
        print("Ok generating programe to find the radius and circumference of a circle..")
    else:
        print("Ok generating programe to check whether a number is even or odd..")
    for _ in range(5):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.3)


import os
def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")

    
def main():
    clear_screen()
    print(" ")
    try:
        choice = int(
            input(
                "\nWhat do you want to do?\n1. Find the circumference and area of a circle.\n2. Add two numbers.\n\nEnter choice:  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if choice == 1:
        circle()
    elif choice == 2:
        add()
    else:
        print("Lean English.")
        x = input("Run again? (y/n)")
        if x == "y":
            main()
        else:
            exit(0)


main()


def circle(radius):
    clear_screen()
    try:
        animation ("circle")
    except NameError: # No such error will happen btw😅.
        print("Processing..")
    circum = 2*3.14*radius
    area= 2*3.14*radius**2
    return circum, area
radius = int(input("Enter the radius: "))
x,y = circle(radius)
print("circum =", x,",","Area =", y)



def add(x,y):
    clear_screen()
    s = x+y
    return s
x = int (input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("Sum of those numbers are: ", add(x,y))

