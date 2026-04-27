import json, os

class TaskManager:
    def __init__(self):
        self.tasks_li = []
        if os.path.exists("tasks.json"):
            try:
                with open("tasks.json", "r") as f:
                    self.tasks_li = json.load(f)
            except:
                pass
    
    def addTask(self):
        title = input("Enter Title: ")
        des = input("Enter Description: ")
        prio = input("Enter Priority (High/Medium/Low): ")

        if (prio in ["High", "Medium", "Low"]):
            data = {
                "title": title,
                "description": des,
                "priority": prio
            }

            self.tasks_li.append(data)
            print("Task added successfully!\n")
            with open("tasks.json", "w") as f:
                json.dump(self.tasks_li, f, indent = 4)
        else:
            print("Invalid input!\n")

    def viewTask(self):
        if len(self.tasks_li) != 0:
            print("========== All Tasks ==========")
            for i in range(0, len(self.tasks_li)):
                print(f"++++++++ Task {i+1} ++++++++")
                print(f"Title: {self.tasks_li[i]['title']}\nDescription: {self.tasks_li[i]["description"]}\nPriority: {self.tasks_li[i]["priority"]}\n")
        else:
            print("No task available!\n")

    def deleteTask(self):
        if len(self.tasks_li) != 0:
            self.viewTask()
            serial_no = int(input("Enter the task no. that you want to delete: "))
            try:
                if serial_no>0:
                    self.tasks_li.pop(serial_no-1)
                    print("Task deleted successfully!\n")
                    with open("tasks.json", "w") as f:
                        json.dump(self.tasks_li, f, indent = 4)
                else:
                    print("Invalid Serial No.!\n")
            except IndexError:
                print("Invalid Serial No.!\n")

        else:
            print("No task available for deletion!\n")

    def updateTaskPriority(self):
        if len(self.tasks_li) != 0:
            self.viewTask()
            serial_no = int(input("Enter task number to update priority: "))
            try:
                if serial_no>0:
                    prio = input("Enter new priority (High/Medium/Low): ")
                    if (prio in ["High", "Medium", "Low"]):
                        self.tasks_li[serial_no-1]["priority"] = prio
                        print("Task priority updated successfully!\n")

                        with open("tasks.json", "w") as f:
                            json.dump(self.tasks_li, f, indent = 4)
                    else:
                        print("Invalid input!\n")
                else:
                    print("Invalid Serial No.!\n")
            except IndexError:
                print("Invalid Serial No.!\n")

        else:
            print("No task available!\n")

obj = TaskManager()
print("===== Task Tracker =====")

while(True):
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Update Task Priority")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice==1:
            obj.addTask()
        elif choice==2:
            obj.viewTask()
        elif choice==3:
            obj.deleteTask()
        elif choice==4:
            obj.updateTaskPriority()
        elif choice==5:
            print("Thank you for using our task manager. Have a great day!")
            break
        else:
            print("Input is not valid!\n")
    except ValueError:
        print("Invalid input!\n")