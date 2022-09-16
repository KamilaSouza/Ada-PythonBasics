# Method 1
archive = open("dom_casmurro_cap_1.txt", "r", encoding="utf-8")
text = archive.read()
print(text)
archive.close()

# Method 2
archive = open("dom_casmurro_cap_1.txt", "r", encoding="utf-8")
line = archive.readline()
while line != "":
    print(line, end="")
    line = archive.readline()
archive.close()

# Method 3
archive = open("dom_casmurro_cap_1.txt", "r", encoding="utf-8")
for line in archive:
    print(line, end="")
archive.close()

# Method 4
with open("dom_casmurro_cap_1.txt", "r", encoding="utf-8") as archive:
    text = archive.read()
    print(text)
