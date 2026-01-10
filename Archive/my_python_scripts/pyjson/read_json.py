import json
w = {
    "name" : "stephan",
    "age"  : 25
}
x = json.load(open("jason-file.json"))
y = json.dumps(w, indent=4)

def create_file():
    with open("test.json", "w") as f:
        f.write(y)
        print("File successfully created!")

def read_file():
    with open("jason-file.json") as f:
        text = f.read()
        text = text.replace("John","Stephan")
        text = text.replace("john","stephan")
        y = json.dumps(text, indent=4)
        print(json.loads(y))


read_file()
# print(y)
