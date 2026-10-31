def save_tasks():
    with open("tasks.json", "w", encoding = "utf-8") as file:
        json.dump(to_do, file)