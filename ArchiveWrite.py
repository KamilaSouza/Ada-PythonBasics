# w Write and create
with open("archive_test.txt", "w", encoding="utf-8") as archive:
    archive.write("Noah is a beautiful guinea pig.\n")
    archive.write("He is cute.\n")

# a Write
with open("archive_test.txt", "a", encoding="utf-8") as archive:
    archive.write("And makes a lot of noise.\n")

# r Read
with open("archive_test.txt", "r", encoding="utf-8") as archive:
    print(archive.read(), end="")
