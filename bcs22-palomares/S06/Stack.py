import time

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.complete = False

class Task_Manager:
    def __init__(self, maximum):
        self.tasks = []
        self.maximum = maximum

    def add(self, title, description):
        new = Task(title, description)
        self.tasks.append(new)
        print("New Task has been included.")
        time.sleep(2)

    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].task_complete = True
            print(f"Task #{index + 1} completed.")
            time.sleep(2)
        else:
            print("Invalid index")
            time.sleep(1)

    def display(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.complete else "Pending"
            print(f"Task #{i + 1}: {'{:<5}'.format(task.title)} - {'{:<5}'.format(task.description)} ({'{:<5}'.format(status)})")
            time.sleep(2)

    def open(self):
        while True:
            print("Task Manager Menu:")
            print("1. Add Task")
            print("2. Mark completed task")
            print("3. Display Tasks")
            print("4. Exit")
            choice = input("Enter your choice: 1, 2, 3, 4 => ")
            print("")

            if choice == "1":
                if len(self.tasks) < self.maximum:
                    title = input("Enter task title: ")
                    description = input("Enter task description: ")
                    self.add(title, description)
                else:
                    print("Your task manager is full.")
                    time.sleep(2)
            elif choice == "2":
                if not self.tasks:
                    print("Task manager is empty.")
                    time.sleep(2)
                else:
                    self.display()
                    index = int(input("Enter task index to be completed: "))
                    self.complete(index - 1)
            elif choice == "3":
                if not self.tasks:
                    print("Task manager is empty")
                    time.sleep(1)
                else:
                    self.display()
            elif choice == "4":
                print("Closing Task Manager...")
                time.sleep(2)
                break
            else:
                print("Invalid choice. Choose again: [1][2][3][4]")
                time.sleep(2)

task_manager = Task_Manager(5)
task_manager.open()