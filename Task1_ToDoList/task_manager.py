import os
fname="Task.txt"

def load():
    task={}
    if (os.path.exists(fname)):
        with open(fname,"r") as f:
            for line in f:
                id,name,status=line.strip().split("-")
                task[int(id)]=[name,status]
    return task

def save(task):
    with open(fname,"w") as f:
        for ids,tasks in task.items():
            f.write(f"{ids}-{tasks[0]}-{tasks[1]}\n")

def add(task):
    id = max(task.keys(),default=0)
    s=input("Enter Your Task: ")
    task[id+1]=[s,"incomplete"]
    print("Task Added.")

def view(task):
    if not task:
        print("No Task Available.")
    else:
        for id,tasks in task.items():
            print(f"[{id}] {tasks[0]} - {tasks[1]}")

def mark(task):
    usrid=int(input("Enter id: "))
    if (usrid in task):
        task[usrid][1]="complete"
        print("Task Marked as Complete.")
    else:
        print("Task id not found.")

def delete(task):
    usrid=int(input("Enter id to Delete: "))
    if (usrid in task):
        if (usrid<max(task.keys())):
            max_id=max(task.keys())
            while (usrid<max_id):
                task[usrid]=task[usrid+1]
                usrid+=1
            task.pop(max_id)
        else:
            task.pop(usrid)
        print("Task deleted.")
    else:
        print("Task id not found.")


task=load()
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    try:
        choice=int(input("Enter your Choice: "))
    except:
        print("Invalid Choice.")
        continue
    if (choice==5):
        save(task)
        print("Task Saved Successfully.")
        break
    elif (choice==1):
        add(task)
    elif (choice==2):
        view(task)
    elif (choice==3):
        mark(task)
    elif (choice==4):
        delete(task)
    else:
        print("Invalid Choice.")
    save(task)