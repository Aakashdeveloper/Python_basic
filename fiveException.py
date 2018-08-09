student = {
    "name": "John",
    "class": "python",
    "rollNo": 12
}

try:
    lastname = student['lastname']
except KeyError:
    print("Error finding lastName")
print("The code is working")