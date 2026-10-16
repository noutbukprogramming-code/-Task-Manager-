import csv


def add_task():
    title = input("Vazifa nomini kiriting: ")
    status = "bajarilmagan"

    with open("tasks.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        tasks = list(reader)
        fieldnames = reader.fieldnames

    new_id = max([int(task["id"]) for task in tasks], default=0) + 1

    with open("tasks.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            "id": new_id,
            "title": title,
            "status": status
        })

    print("Vazifa muvaffaqiyatli qo‘shildi!")

if __name__ == "__main__":
    add_task()