import csv

# with open("brasil_covid.csv", "r", encoding="utf-8") as archive_csv:
#    reader = csv.reader(archive_csv)
#    header = next(reader)
#    for line in reader:
#        if float(line[2]) > 1:
#            print(line)

with open("users.csv", "w", encoding="utf=8", newline="") as users_archive:
    writer = csv.writer(users_archive)
    writer.writerow(["name", "lastname", "email", "gender"])
    writer.writerow(["Kamila", "Souza", "kamila@email.com", "female"])


header = ["name", "lastname"]
data = []
output = input("What do you wanna do?\n1 - Register?\n0 - Leave\n")
while output != "0":
    name = input("What is your name?")
    lastname = input("What is your lastname?")
    data.append([name, lastname])
    output = input("What do you wanna do?\n1 - Register?\n0 - Leave\n")

print(data)

with open("users1.csv", "w", newline="") as archive_csv:
    writer = csv.writer(archive_csv)
    writer.writerow(header)
    writer.writerow(data)

with open("users1.csv", "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row)
