#for number in range(1,1001)
#print(number)

students={
    "male":["tome","Charlie","Harry","Frank"],
    "female":["Sarah","Huda","Samantha","Emily","Elizabeth"]
    }

for key in students.keys():
    for name in students[key]:
        if "b" in name:
            print(name)
