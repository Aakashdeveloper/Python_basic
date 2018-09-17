city = ("london", "hongkong", "newyork", "hongkong")
>>> city = ("london", "hongkong", "newyork")
>>> city
('london', 'hongkong', 'newyork')
>>> city[1]
'hongkong'
>>> city[2]
'newyork'
>>> city[1]="amsterdam"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> city = ("london", "hongkong", "newyork", "hongkong")
>>> city
('london', 'hongkong', 'newyork', 'hongkong')
>>> len(city)
4
>>> 
colors = tuple(("red", "yellow", "green"))