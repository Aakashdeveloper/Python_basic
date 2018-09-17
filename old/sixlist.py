list=> data can be manupulated as well as can have duplicate value
tuple => value cannot change but duplicate members allowed
set => no duplicate memeber allowed & unindexed
dictionary => changeable, not allow duplicate value & indexed


cars = ["bmw", "audi", "volvo"]
>>> cars = ["bmw", "audi", "volvo"]
>>> cars
['bmw', 'audi', 'volvo']
>>> cars[0]
'bmw'
>>> cars[1]
'audi'
>>> cars[1]="kia"
>>> cars
['bmw', 'kia', 'volvo']
>>> cars[3]="audi"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> cars = ["bmw", "audi", "volvo"]
>>> cars[1]="bmw"
>>> cars
['bmw', 'bmw', 'volvo']
>>> cars.append("kia")
>>> cars
['bmw', 'bmw', 'volvo', 'kia']
>>> cars.remove("bmw")
>>> cars
['bmw', 'volvo', 'kia']
>>> len(cars)
3
>>> cars.sort()
>>> cars
['bmw', 'kia', 'volvo']
>>> cars.reverse()
>>> cars
['volvo', 'kia', 'bmw']
>>> cars.index("kia
  File "<stdin>", line 1
    cars.index("kia
                  ^
SyntaxError: EOL while scanning string literal
>>> cars.index("kia")
1
>>> cars.clear()
>>> cars
[]
>>> cars = ["bmw", "audi", "volvo"]
>>> cars.pop(1)
'audi'
>>> cars
['bmw', 'volvo']

lang = list(("python", "angularJs", "nodejs"))
