import os
fname="Task.txt"

def load():
    tasks=[]
    if (os.path.exists(fname)):
        with open(fname,"r") as f:
            for task in f:
                temp=task.strip().split("-")
                temp[0]=int(temp[0])
                tasks.append(temp)
    return tasks

def save(tasks):
    with open(fname,"w") as f:
        for task in tasks:
            f.write(f"{task[0]}-{task[1]}-{task[2]}\n")

def add(tasks):
    s=input("Enter Your Task: ")
    tasks.append([len(tasks)+1,s,"Incomplete"])
    print("Task Added.")

def view(tasks):
    if not tasks:
        print("No Task Available.")
    else:
        for task in tasks:
            print(f"[{task[0]}] {task[1]} - {task[2]}")

def mark(tasks):
    if not tasks:
        print("No Task Available.")
        return
    else:
        usrid=int(input("Enter id: "))
        for task in tasks:
            if (task[0]==usrid):
                task[2]="Complete"
                print("Task marked as Complete.")
                return
    print("Task ID not Found.")
    

def delete(tasks):
    if not tasks:
        print("No Task Available.")
        return
    else:
        usrid=int(input("Enter id: "))
        for i in range(len(tasks)):
            if (tasks[i][0]==usrid):
                tasks.pop(i)
                for j in range(i, len(tasks)):
                    tasks[j][0] -= 1
                print("Task deleted.")
                return
    print("Task ID not Found.")

tasks=load()
while True:
    try: 
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice=int(input("Enter your Choice: "))
        if (choice==5):
            save(tasks)
            print("Task Saved Successfully.")
            break
        elif (choice==1):
            add(tasks)
        elif (choice==2):
            view(tasks)
        elif (choice==3):
            mark(tasks)
        elif (choice==4):
            delete(tasks)
        else:
            print("Invalid Choice.")
        save(tasks)
    except:
        print("Enter a Valid Answer.")