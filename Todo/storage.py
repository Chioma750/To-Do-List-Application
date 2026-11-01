import json
import load_tasks()

to_do = []

def save_tasks():
    with open("tasks.json", "w", encoding = "utf-8") as file:
        json.dump(to_do, file)

def load_tasks():
    try:
        with open("tasks.json", "r", encoding = "utf-8") as file:
            reading = json.load(file)
            to_do.extend(reading)
    except FileNotFoundError:
        pass

load_tasks()
