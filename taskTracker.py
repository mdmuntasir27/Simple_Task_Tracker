class TaskManager:
    def __init__(self):
        self.tasks_li = []
    
    def addTask(self):
        title = input("Enter Title: ")
        des = input("Enter Description: ")

        data = {
            "title": title,
            "description": des
        }

        self.tasks_li.append(data)
        print("Task added successfully!\n")

    def viewTask(self):
        if len(self.tasks_li) != 0:
            print("========== All Tasks ==========")
            for i in range(0, len(self.tasks_li)):
                print(f"++++++++ Task {i+1} ++++++++")
                print(f"Title: {self.tasks_li[i]['title']}\nDescription: {self.tasks_li[i]["description"]}\n")
        else:
            print("No task available!\n")

    def deleteTask(self):
        if len(self.tasks_li) != 0:
            self.viewTask()
            serial_no = int(input("Enter the task no. that you want to delete: "))
            try:
                self.tasks_li.pop(serial_no-1)
                print("Task deleted successfully!\n")
            except ValueError:
                print("Input is not valid!\n")
            except IndexError:
                print("Enter a valid serial no.!\n")

        else:
            print("No task available for deletion!\n")

obj = TaskManager()
print("===== Task Tracker =====")

while(True):
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice==1:
            obj.addTask()
        elif choice==2:
            obj.viewTask()
        elif choice==3:
            obj.deleteTask()
        elif choice==4:
            print("Thank you for using our task manager! Have a great day!")
            break
        else:
            print("Input is not valid!\n")
    except ValueError:
        print("Input is not valid!\n")