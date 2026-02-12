#1
import csv
with open ("data.txt", "r") as h:
    lines = [line.strip() for line in h]
with open ("data.csv","w",newline="") as w:
    writer = csv.writer(w)
    writer.writerows([""])
    for line in lines:
        writer.writerow([line])
#2
import csv
with open ("file.txt", "r") as h:
    lines = [line.strip() for line in h]
    with open("file.csv", "w", newline="") as w:
        writer = csv.writer(w)
        writer.writerows([""])
        for line in lines:
            writer.writerow([line])

#3
import csv
with open ("name.txt", "r") as h:
    lines = [line.strip() for line in h]
    with open("name.csv", "w", newline="") as w:
        writer = csv.writer(w)
        writer.writerows([""])
        for line in lines:
            writer.writerow([line])