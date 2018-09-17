marks = 42
name = "charan"
answer = False
#int marks = 42
#String name = "Charan"

#string => any thing inside double quotes("",'') ('"/ "')
#number => any number like 1, 2 46 
#boolean => True or False

random = '6789'
pi = 3.145

city = "london"
country = "England"
>>> city + country
'londonEngland'

>>> subject = "Maths"
>>> marks = 20
>>> subject + marks
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> marks + subject
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> marks = 20
>>> marks1 = 30
>>> marks + marks1
50
>>> pi = 3.145
>>> int(pi)
3
>>> int(pi) == 3
True
>>> int(pi) == 3.145
False
>>> float(pi)== 3.145
True
>>> float(pi)
3.145
>>> int(pi)
3
>>> int(marks1) == 30.00
True
>>> int(marks1) == 30.123
False
>>> 


= is assignment
== is comprasion

' Hi Python ' == " Hi Python"

>>> ' Hi Python ' == " Hi Python"
False
>>> 'Hi Python' == "Hi Python"
True
>>> 'Hi Python' == "Hi Python" == """Hi Python"""
True
>>> 