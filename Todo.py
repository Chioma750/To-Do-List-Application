to_do = []
def add_task():
    answer = input("What is your task for today: ")

    task = {
        "text": answer,
        "done": False,
    }
    to_do.append(task)
    print("Added")

def view_task():
    for num, task in enumerate(to_do, start = 1):
        print (num, task["text"])
add_task()
add_task()
print()
view_task()

#print(to_do)