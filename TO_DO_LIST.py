def main():
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f'Task "{task}" added to the list.')
        elif choice == '2':
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f'Task "{task}" removed from the list.')
            else:
                print(f'Task "{task}" not found in the list.')
        elif choice == '3':
            if not tasks:
                print("No tasks in the list.")
            else:
                print("To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()