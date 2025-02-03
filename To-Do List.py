'''
Dario Sanai
sanaidario@gmail.com
Personal Project
To-Do List 2/2/2025
'''

# It is necessary to have a text file named "To.Do List" piped to the program for it to work
# The text file must already be three lines long when the program is used for the very first time
# The first line of the text file must start with the title (i.e. To-Do List)
# The second and third line of the text file must be blank

def main():

    taskList = []
    taskFileList = open("To-Do List.txt", "r")
    for line in taskFileList:
        line = line.strip()
        taskList.append(line)
    taskFileList.close()
    print("Dario's To-Do List")

    while True:

        userChoice = input("\nChoose an option:\n1. Display tasks\n2. Add tasks\n3. Delete tasks\n4. End program\n\n")

        if userChoice == "1":
            if len(taskList) < 3:
                print("\nAll tasks complete!")
            else:
                taskString = "\n".join(taskList)
                print("\n" + taskString)

        elif userChoice == "2":
            userAdd = input("\nAdd a task: ")
            taskFileAdd = open("To-Do List.txt", "a")
            print("• " + userAdd, file=taskFileAdd)
            taskFileAdd.close()
            print("Task added successfully!")
            taskList.append("• " + userAdd)

        elif userChoice == "3":
            if len(taskList) < 3:
                print("\nNo tasks to delete!")
            else:
                while True:
                    userDelete = input("\nPlease input the number of the task you want to delete: ")
                    if userDelete.isdigit():
                        userDeleteInt = int(userDelete)
                        if userDeleteInt > 0 and userDeleteInt < len(taskList) - 1:
                            del taskList[userDeleteInt + 1]
                            taskStringDelete = "\n".join(taskList)
                            taskFileDelete = open("To-Do List.txt", "w")
                            print(taskStringDelete, file=taskFileDelete)
                            taskFileDelete.close()
                            print("Task deleted successfully!")
                            break
                        else:
                            print("Invalid response.")
                    else:
                        print("Invalid response.")

        elif userChoice == "4":
            print("\nGoodbye!")
            break

        else:
            print("\nPlease choose a number between 1 and 4.")

if __name__ == '__main__':
    main()