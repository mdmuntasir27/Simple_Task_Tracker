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

        data = {
            "title": title,
            "description": des,
            "completed": False
        }

        self.tasks_li.append(data)
        print("Task added successfully!\n")
        with open("tasks.json", "w") as f:
            json.dump(self.tasks_li, f, indent = 4)

    def viewTask(self):
        if len(self.tasks_li) != 0:
            print("========== All Tasks ==========")
            for i in range(0, len(self.tasks_li)):
                print(f"++++++++ Task {i+1} ++++++++")
                if self.tasks_li[i]['completed'] == False:
                    print(f"Title: {self.tasks_li[i]['title']}\nDescription: {self.tasks_li[i]["description"]}\nStatus: Not Completed\n")
                else:
                    print(f"Title: {self.tasks_li[i]['title']}\nDescription: {self.tasks_li[i]["description"]}\nStatus: Completed\n")
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

    def updateTaskStatus(self):
        if len(self.tasks_li) != 0:
            self.viewTask()
            serial_no = int(input("Enter task number to mark as completed: "))
            try:
                if serial_no>0:
                    if(self.tasks_li[serial_no-1]['completed'] == False):
                        self.tasks_li[serial_no-1]['completed'] = True
                        print("Task marked as completed!\n")
                    else:
                        print("The task is already completed!\n")

                    with open("tasks.json", "w") as f:
                        json.dump(self.tasks_li, f, indent = 4)
                else:
                    print("Invalid Serial No.!\n")
            except IndexError:
                print("Invalid Serial No.!\n")

        else:
            print("No task available to mark completed!\n")

obj = TaskManager()
print("===== Task Tracker =====")

while(True):
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Mark Task as Completed")
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
            obj.updateTaskStatus()
        elif choice==5:
            print("Thank you for using our task manager. Have a great day!")
            break
        else:
            print("Input is not valid!\n")
    except ValueError:
        print("Invalid input!\n")