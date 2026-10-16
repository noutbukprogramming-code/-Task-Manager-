import csv


def show_tasks():
    with open("tasks.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for task in reader:
            print(
                f"ID: {task['id']} | "
                f"Vazifa: {task['title']} | "
                f"Holati: {task['status']}"
            )

if __name__ == "__main__":
    show_tasks()