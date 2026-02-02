import csv
while True:
    try:
        with open ("notes/reading.txt","r") as file:
            for line in file:
                print(f"Hello{line.strip()}")
    except:
        print("that file can't be found")

    else:
        print("code ends")
        break

try:
    with open("notes/sample.csv", mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = line
        rows = []
        for line in content:
            rows.append({headers[0]: line[0],headers[1]: line[1]})
except:
    print("we cant find that file")
else:
    for line in rows:
        print(line)