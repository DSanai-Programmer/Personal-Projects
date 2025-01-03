'''
Dario Sanai
sanaidario@gmail.com
Personal Project
Tic-Tac-Toe 1/2/2025
'''

import random

def main():

    print("Welcome to Tic-Tac-Toe!")
    userInput = "Y"

    while userInput == "Y":

        a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
        numberList = [a, b, c, d, e, f, g, h, i]

        while True:

            print()
            print(a, "|", b, "|", c)
            print("---------")
            print(d, "|", e, "|", f)
            print("---------")
            print(g, "|", h, "|", i)

            userChoice = input("\nChoose a number: ")
            userChoiceString = str(userChoice)

            while True:
                if userChoiceString.isdigit():
                    userChoice = int(userChoice)
                    if userChoice in numberList:
                        break
                    else:
                        userChoice = input("Faulty input. Choose a number: ")
                        userChoiceString = str(userChoice)
                else:
                    userChoice = input("Faulty input. Choose a number: ")
                    userChoiceString = str(userChoice)

            if userChoice == a:
                numberList.remove(userChoice)
                a = "X"
            elif userChoice == b:
                numberList.remove(userChoice)
                b = "X"
            elif userChoice == c:
                numberList.remove(userChoice)
                c = "X"
            elif userChoice == d:
                numberList.remove(userChoice)
                d = "X"
            elif userChoice == e:
                numberList.remove(userChoice)
                e = "X"
            elif userChoice == f:
                numberList.remove(userChoice)
                f = "X"
            elif userChoice == g:
                numberList.remove(userChoice)
                g = "X"
            elif userChoice == h:
                numberList.remove(userChoice)
                h = "X"
            elif userChoice == i:
                numberList.remove(userChoice)
                i = "X"

            if ((a, b, c) == ("X", "X", "X") or (d, e, f) == ("X", "X", "X") or (g, h, i) == ("X", "X", "X") or (a, d, g) == ("X", "X", "X")
             or (b, e, h) == ("X", "X", "X") or (c, f, i) == ("X", "X", "X") or (a, e, i) == ("X", "X", "X") or (c, e, g) == ("X", "X", "X")):
                print()
                print(a, "|", b, "|", c)
                print("---------")
                print(d, "|", e, "|", f)
                print("---------")
                print(g, "|", h, "|", i)
                print("\nYou win!")
                break

            if len(numberList) == 0:
                print()
                print(a, "|", b, "|", c)
                print("---------")
                print(d, "|", e, "|", f)
                print("---------")
                print(g, "|", h, "|", i)
                print("\nIt's a tie!")
                break

            computerChoice = random.choice(numberList)

            if computerChoice == a:
                numberList.remove(computerChoice)
                a = "O"
            elif computerChoice == b:
                numberList.remove(computerChoice)
                b = "O"
            elif computerChoice == c:
                numberList.remove(computerChoice)
                c = "O"
            elif computerChoice == d:
                numberList.remove(computerChoice)
                d = "O"
            elif computerChoice == e:
                numberList.remove(computerChoice)
                e = "O"
            elif computerChoice == f:
                numberList.remove(computerChoice)
                f = "O"
            elif computerChoice == g:
                numberList.remove(computerChoice)
                g = "O"
            elif computerChoice == h:
                numberList.remove(computerChoice)
                h = "O"
            elif computerChoice == i:
                numberList.remove(computerChoice)
                i = "O"

            if ((a, b, c) == ("O", "O", "O") or (d, e, f) == ("O", "O", "O") or (g, h, i) == ("O", "O", "O") or (a, d, g) == ("O", "O", "O") or
                (b, e, h) == ("O", "O", "O") or (c, f, i) == ("O", "O", "O") or (a, e, i) == ("O", "O", "O") or (c, e, g) == ("O", "O", "O")):
                print()
                print(a, "|", b, "|", c)
                print("---------")
                print(d, "|", e, "|", f)
                print("---------")
                print(g, "|", h, "|", i)
                print("\nYou lose!")
                break

        userInput = input("\nWould you like to play again (Y/N)? ").upper()
        while userInput != "Y" and userInput != "N":
            userInput = input("Invalid response. Would you like to play again (Y/N)? ").upper()

    print("\nCome again!")

if __name__ == '__main__':
    main()