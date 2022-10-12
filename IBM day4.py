Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={"name":["mahak","mayuri","kejal"],"age":[19,20,18],}
type(d1)
<class 'dict'>
len(d1)
2
d1[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d1[0]
KeyError: 0
d1["name"]
['mahak', 'mayuri', 'kejal']
d1["age"]
[19, 20, 18]
d1.keys()
dict_keys(['name', 'age'])
dict_keys(['name', 'age'])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict_keys(['name', 'age'])
NameError: name 'dict_keys' is not defined
d1.values()
dict_values([['mahak', 'mayuri', 'kejal'], [19, 20, 18]])
d1.items()
dict_items([('name', ['mahak', 'mayuri', 'kejal']), ('age', [19, 20, 18])])
print(d1)
{'name': ['mahak', 'mayuri', 'kejal'], 'age': [19, 20, 18]}
d1["ph_no."] = 2223355,8855444,6677844
d1
{'name': ['mahak', 'mayuri', 'kejal'], 'age': [19, 20, 18], 'ph_no.': (2223355, 8855444, 6677844)}
d1["name"]
['mahak', 'mayuri', 'kejal']
d1["name"][0]
'mahak'
d1["name"][0][1:-6]
''
d1["name"][0][0:-5]
''
d1["name"][0:-5]
[]
d1["name"][0][-6:-1]
'maha'
d1["name"][0][-1:-6]
''
''
''
d1["name"][0][-1::-1]
'kaham'
'kaham'
'kaham'
d1+=["new val"]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d1+=["new val"]
TypeError: unsupported operand type(s) for +=: 'dict' and 'list'
d1.append("abc")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d1.append("abc")
AttributeError: 'dict' object has no attribute 'append'
d1.add("abc")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d1.add("abc")
AttributeError: 'dict' object has no attribute 'add'
del d1["ph_no"]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    del d1["ph_no"]
KeyError: 'ph_no'
d1
{'name': ['mahak', 'mayuri', 'kejal'], 'age': [19, 20, 18], 'ph_no.': (2223355, 8855444, 6677844)}
del d1["ph_no"]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    del d1["ph_no"]
KeyError: 'ph_no'
print(d1)
{'name': ['mahak', 'mayuri', 'kejal'], 'age': [19, 20, 18], 'ph_no.': (2223355, 8855444, 6677844)}
d1
{'name': ['mahak', 'mayuri', 'kejal'], 'age': [19, 20, 18], 'ph_no.': (2223355, 8855444, 6677844)}
del d1["ph_no"]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    del d1["ph_no"]
KeyError: 'ph_no'
del d1['ph_no']
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    del d1['ph_no']
KeyError: 'ph_no'
del d1["ph_no."]
d1
{'name': ['mahak', 'mayuri', 'kejal'], 'age': [19, 20, 18]}
print(d1)
{'name': ['mahak', 'mayuri', 'kejal'], 'age': [19, 20, 18]}
d1.get("email")
d1.get("name")
['mahak', 'mayuri', 'kejal']
a=20
b="ml"
print(a,b)
20 ml
print(a,b,sep="    ")
20    ml
print(a,b,sep="@")
20@ml
print(a)
20

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
20####ml

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
20
ml
a=input("enter your name:  ")
enter your name:  mahak
a
'mahak'
x="enter first number:
SyntaxError: unterminated string literal (detected at line 1)
x="enter first no."
y="enter second no."
z="sum"
m=input("x,y,z")
x,y,zm
m=input()
m=input(x)
x
'enter first no.'
23
23
m=input(y)
enter second no.45
m=input(z)
sum
z="x+y"
m=input(z)
x+y
34
34
78
78
m=input(45)
45
m=input(78)
78
m=input(z)
x+y
z
'x+y'
input(z)
x+y
''
''
''
if age<18:
     print("a gift")
if age>=18 and age<=20:
     print("a gift")
     print("a task")
if age>20:
     print("koi gift nahi hai")
     
SyntaxError: invalid syntax
if age<18:
    print("a gift")
if age>=18 and age<=20:
    print("a gift")
    print("a task")
if age>20:
    print("koi gift nahi hai")
    
SyntaxError: invalid syntax
age=input("enter your age")
if age<18:
   print("a gift")
if age>=18 and age<=20:
   print("a gift")
   print("a task")
if age>20:
   print("koi gift nahi hai")  SyntaxError: invalid syntax
   
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax

age=int("input your age")
if age<18:
   print("a gift")
if age>=18 and age<=20:
   print("a gift")
   print("a task")
if age>20:
   print("koi gift nahi hai")
   
SyntaxError: multiple statements found while compiling a single statement
age=int(input("enter your age"))
if age<18:
   print("a gift")
if age>=18 and age<=20:
   print("a gift")
   print("a task")
if age>20:
   print("koi gift nahi hai")
   
SyntaxError: multiple statements found while compiling a single statement
if age<18:
    print("a gift")
elif age>=18 and age<=20:
    print("a gift")
    print("a task")
else:
    print("koi gift nahi hai")
    print(age)
    age
if today=="saturday":
     print("half day work")
elif today=="sunday":
     if condition=="sick":
             print("take rest")
     else:
         print("party")
         
SyntaxError: invalid syntax

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py", line 1, in <module>
    int(input("enter your age"))
ValueError: invalid literal for int() with base 10: ''
89
89

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age67
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py", line 2, in <module>
    if today=="saturday":
NameError: name 'today' is not defined

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age89
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py", line 2, in <module>
    if age<18:
NameError: name 'age' is not defined

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age89
koi gift nahi hai
34
34

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age34
koi gift nahi hai
enter your age78
koi gift nahi hai

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age7
a gift
enter your age2
a gift
enter your age1
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py", line 18, in <module>
    if today=="saturday":
NameError: name 'today' is not defined

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age3
a gift
enter your age5
a gift
enter your agesaturday
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py", line 17, in <module>
    today=int(input("enter your age"))
ValueError: invalid literal for int() with base 10: 'saturday'

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age6
a gift
enter your age3
a gift
enter the daysunday
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py", line 17, in <module>
    today=int(input("enter the day"))
ValueError: invalid literal for int() with base 10: 'sunday'

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py
enter your age8
a gift
enter your age90
koi gift nahi hai
enter the daysaturday
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/IBM day4 new file.py", line 17, in <module>
    day=int(input("enter the day"))
ValueError: invalid literal for int() with base 10: 'saturday'
range(0,11)
range(0, 11)
list(range(0,11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
