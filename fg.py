#1
with open ("data.txt", "w") as h:
    h.write("hello\n")
    h.write("world\n")
#2
with open ("file.txt", "w") as h:
    for i in range (1,11):
        h.write(str(i) + "\n")

#3
with open ("name.txt", "w") as h:
    name = input()

    for n in name.split():
        h.write(n.title() + "\n")
print("saved")