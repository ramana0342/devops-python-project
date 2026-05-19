import csv

print("Employee Details")
print("------------------")

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            f"ID: {row['id']} | "
            f"Name: {row['name']} | "
            f"Role: {row['role']}"
        )