import csv

# Writing to a CSV file
#with open used to open or do som actions in it
                          #mode="w" used to write
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Hari", 95])
    writer.writerow(["Shri", 90])

# Reading from the CSV file
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



#json file handling
import json

# Data to write
data = {
    "students": [
        {"name": "Navin", "marks": 90},
        {"name": "Hari", "marks": 80}
    ]
}

# Writing to a JSON file
#open with helps us to create the json file "W" used to write
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)    #this json.dump used to write Python data to a JSON file.

# Reading from the JSON file
with open("students.json", "r") as file:
    content = json.load(file)
    print(content)
