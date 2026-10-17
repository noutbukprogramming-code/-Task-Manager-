import csv

def complete_task():
    task_id = input("ID ni kiriting: ")
    tasks=[]

    with open("tasks.csv", "r",newline="",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames= reader.fieldnames
        tasks = list(reader)

        found = False
        for task in tasks:
            if task["ID"] == task_id:
                task["status"]="bajarilgan"
                found=True
                break
        if found:
            with open("tasks.csv", "w", newline="",encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(tasks)
            print("vazifa bajarilgan deb belgilandi!")
        else:
            print("bunday ID topilmadi.")

            if __name__ == "__main__":
                complete_task()
            

        
