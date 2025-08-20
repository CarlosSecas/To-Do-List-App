# Intialize an empty list to strore user tasks
tasks = []

def addTask():
    # Ask for user input and store it in a variable
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def listTasks():
    # Check if anything is in the list
    if not tasks:
        print("THere are no tasks currently")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index+1}. {task}")

def deleteTask():
    # Call listTask() to provide the list of tasks user has added
    listTasks()
    try:
        taskToDelete = int(input("PLease enter a # to delete that task: "))
        # will go through if input is not negative and if input is within the length of the list.
        taskIndex = taskToDelete - 1
        if taskIndex >= 0 and taskIndex < len(tasks):
            taskRemoved = tasks.pop(taskIndex)
            print(f"Task '{taskRemoved}' has been removed.")
        else:
            print(f"Task '{taskToDelete}' was not found.")
    
    except:
        # if user entered a number that did not belong a task
        print("Invalid input.")


# Main method
if __name__ == "__main__":
    # Create a loop to run the app
    print("Welcome to the to do list app :)")
    # Run app until user says no
    while True:
        print("\n")
        print("Please select one of the following options")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try agian")

    print("Goodbye!")



