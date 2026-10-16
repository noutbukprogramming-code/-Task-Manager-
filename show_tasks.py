import csv

with open("tasks.csv", "r") as f:
    data = csv.reader(f)

    for key in data:
        print(key)