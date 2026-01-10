import json
x = {
    "name" : "stephan",
    "age" : 25
}

#print(x)
x["rollno"] = 22
x["gender"] = "male"
#print(x)

json_file = "pydict.json"

def save_file(key, value):
    with open(json_file, "w") as f:
        x[key] = value
        y = json.dumps(x, indent=4)
        f.write(y)
        print("File Saved as {}".format(json_file))

def read_file():
    with open(json_file,"r") as f:
        print("Reading from : {}".format(json_file))
        print(f.read())

save_file("country","India")
save_file("Nationality","America")

read_file()

