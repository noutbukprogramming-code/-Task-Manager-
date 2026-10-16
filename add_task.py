import csv

with open("tasks.csv", "a") as f:
    writer = csv.writer(f)

    name = input("Name: ")
    status = input("Status: ")
    id = int(input("ID: "))
    writer.writerow([id, name, status])

print("Odam muvaffaqiyatli qo'shildi!")