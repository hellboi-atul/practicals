import os
from time import sleep


def animation(x):
    if x == "circle":
        print("Ok generating programe to find the area and circumference of a circle..")
    else:
        print("Ok generating programe to check whether a number is even or odd..")
    for _ in range(3):
        for frame in r"-\|/-\|/-":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.3)


def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def circle(radius):
    clear_screen()
    animation("circle")
    circum = 2 * 3.14 * radius
    area = 2 * 3.14 * radius ** 2
    return circum, area


def add(x, y):
    return x + y


def restart():
    x = input("Run again? (y/n) :  ")
    if x == "y":
        main()
    else:
        exit(1)


def main():
    clear_screen()
    print(" ")
    choice = input(
        "\nWhat do you want to do?\n1. Find the circumference and area of a circle.\n2. Add two numbers.\n\nEnter choice:  "
    )
    if choice == "1":
        radius = int(input("Enter the radius: "))
        x, y = circle(radius)
        print("\n\ncircumference =", x, "\n", "Area =", y)
        restart()
    elif choice == "2":
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print("\n\nSum of those numbers are: ", add(x, y))
        restart()
    else:
        print("Learn English.")
        sleep(0.5)
        restart()


main()
