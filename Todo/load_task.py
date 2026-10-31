def load_tasks():
    try:
        with open("tasks.json", "r", encoding = "utf-8") as file:
            reading = json.load(file)
            to_do.extend(reading)
    except FileNotFoundError:
        pass

load_tasks()
