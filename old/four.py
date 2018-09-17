Dictionaries

student = {
    "name": "John",
    "class": "python"
}
student["name"] = "Sammy"

student["name"] == "Sammy"

list 

allStudent = [
    {"name": "John", "class": "python"},
    {"name": "John", "class": "python"}
]

fruits = ["Apple", "Mango", "banana"]



##################
Type "help", "copyright", "credits" or "license" for more information.
>>> student = {
...     "name": "John",
...     "class": "python"
... }
>>> student
{'name': 'John', 'class': 'python'}
>>> student.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'name'
>>> fruits = ["Apple", "Mango", "banana"]
>>> fruits
['Apple', 'Mango', 'banana']
>>> fruits[0]
'Apple'
>>> student["name"]
'John'
>>> student["name"] = "Sammy"
>>> student
{'name': 'Sammy', 'class': 'python'}
>>> student["last_name"] = "Sammy"
>>> student
{'name': 'Sammy', 'class': 'python', 'last_name': 'Sammy'}
>>> student["name"] == "Sammy"
True
>>> student["name"] == "Sammky"
False
>>> student["city"] == "Sammky"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'city'
>>> student.get('city')
>>> student.get('city', "Unkown") == "Unkown
  File "<stdin>", line 1
    student.get('city', "Unkown") == "Unkown
                                           ^
SyntaxError: EOL while scanning string literal
>>> student.get('city', "Unkown") == "Unkown"
True
>>> student
{'name': 'Sammy', 'class': 'python', 'last_name': 'Sammy'}
>>> del student["class"]
>>> student
{'name': 'Sammy', 'last_name': 'Sammy'}
>>> 


list
cars = ["bmw", "volvo", "audi", "kia"]
for a in cars:
  print(a)

#####
for(i=0;i<cars.length;i++){
  console.log(cars[i])
}
