Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="hello world"
print(a)
hello world
a[0]
'h'
a[6]
'w'
a[11]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[11]
IndexError: string index out of range
a[10]
'd'
a[-1]
'd'
a="hello world"
a[0:2]
'he'
a[0:6]
'hello '
a[0:8]
'hello wo'
a[0:-6]
'hello'
a[0:-8]
'hel'
a[0:-9]
'he'
a[starting point(by default 0)(including):stop:step]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
[starting point(by default 0):stop(excluding):step(b.d1](including)
 
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
[starting point(by default 0):stop(excluding):step(b.d1)(including)]
 
SyntaxError: invalid syntax. Perhaps you forgot a comma?
[starting point(by default 0):stop(excluding):step(b.d1)(including)
 
SyntaxError: invalid syntax. Perhaps you forgot a comma?

a[0:2]
 
'he'
a[:2]
 
'he'
a[:2:1]
 
'he'
a[:10:2]
 
'hlowr'
a[6:11]
 
'world'
a[-5:]
 
'world'
a[6:]
 
'world'
a
 
'hello world'
a[6:1111111]
 
'world'
a[6:12]
 
'world'
a[7:11]
 
'orld'
dlrow olleh
 
SyntaxError: invalid syntax
#dlrow olleh
 
a[-1::-1]
 
'dlrow olleh'
a[::-1]
 
'dlrow olleh'
a[::-2]
 
'drwolh'
a[-2::-2]
 
'lo le'
a[-3::-3]
 
'r l'
a[-1::-2]
 
'drwolh'
a[-3]
 
'r'
a[:-3]
 
'hello wo'
a[-8:-6]
 
'lo'
a
 
'hello world'
a[-7:-6]
 
'o'
a="hello world"
 
a.capitalize()
 
'Hello world'
a
 
'hello world'
a=a.capitalize()
 
a
 
'Hello world'
a="hello world"
 
a.title()
 
'Hello World'
a.center(50)
 
'                   hello world                    '
a.center(50,"#")
 
'###################hello world####################'
a.count{"1")
 
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a.count("1")
 
0
a=a.center(50)
 
a
 
'                   hello world                    '
a.lstrip()
 
'hello world                    '
a.rstip()
 
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.rstip()
AttributeError: 'str' object has no attribute 'rstip'. Did you mean: 'rstrip'?
a.rstrip()
 
'                   hello world'
a=a.strip()
 
a
 
'hello world'
a.isupper()
 
False
a.islower()
 
True
a=a.upper()
 
a
 
'HELLO WORLD'
a.lower()
 
'hello world'
a.startswith("he")
 
False
a
 
'HELLO WORLD'
a.endswith('D')
 
True
len(a)
 
11
a
 
'HELLO WORLD'
a[0]='M'
 
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a[0]='M'
TypeError: 'str' object does not support item assignment
del a(0]
 
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
del a[0]
 
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    del a[0]
TypeError: 'str' object doesn't support item deletion
b= 'akshat123@gmail.com'
 
b.split("@")
 
['akshat123', 'gmail.com']
b
 
'akshat123@gmail.com'
b=b.split("@")
 
b
 
['akshat123', 'gmail.com']
"@".join(b)
 
'akshat123@gmail.com'
x="mahak"
 
x.split("h")
 
['ma', 'ak']
x.split("m")
 
['', 'ahak']
x
 
'mahak'
"a".join(x)
 
'maaahaaak'
'maaahaaak'
 
'maaahaaak'
###########################################################################
 
m=[12,'hi',2.3,500]
 
m[0]
 
12
m[1:3]
 
['hi', 2.3]
m[0:2]
 
[12, 'hi']
'hi' in m
 
True
'hello' in m
 
False
'hi' not in m
 
False
2*m
 
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
m+=['new val']
 
m
 
[12, 'hi', 2.3, 500, 'new val']
m.append('abc')
 
m
 
[12, 'hi', 2.3, 500, 'new val', 'abc']
m.append('x','y')
 
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    m.append('x','y')
TypeError: list.append() takes exactly one argument (2 given)
m.extend(['x','y','kuch bhi'])
 
m
 
[12, 'hi', 2.3, 500, 'new val', 'abc', 'x', 'y', 'kuch bhi']
m.insert('hello',2)
 
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    m.insert('hello',2)
TypeError: 'str' object cannot be interpreted as an integer
m.instert(2,'hello')
 
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    m.instert(2,'hello')
AttributeError: 'list' object has no attribute 'instert'. Did you mean: 'insert'?
m.insert(2,'hello')
 
m
 
[12, 'hi', 'hello', 2.3, 500, 'new val', 'abc', 'x', 'y', 'kuch bhi']
m.pop()
 
'kuch bhi'
m
 
[12, 'hi', 'hello', 2.3, 500, 'new val', 'abc', 'x', 'y']
m.pop()
 
'y'
m
 
[12, 'hi', 'hello', 2.3, 500, 'new val', 'abc', 'x']
mp=m.pop()
 
mp
 
'x'
m.pop(0)
 
12
m
 
['hi', 'hello', 2.3, 500, 'new val', 'abc']
m.clear()
 
m
 
[]
n=[12,45,52,100]
 
n.reverse()
 
n
 
[100, 52, 45, 12]
n.sort()
 
n
 
[12, 45, 52, 100]
z=[34,90,16,54,66]
 
z.sort()
 
z
 
[16, 34, 54, 66, 90]
max(z)
 
90
min(z)
 
16
n
 
[12, 45, 52, 100]
m
 
[]
m=[12,'hi',2.3,500,'new val']
 
m.index('hi')
 
1
m.index(500)
 
3
m[1][0]
 
'h'
m[4][1]
 
'e'
####################################################################################
 
t=52,23,'abc'
 
type(t)
 
<class 'tuple'>
len(t)
 
3
t.index('abc')
 
2
t[0]
 
52
t
 
(52, 23, 'abc')
t[:2]
 
(52, 23)
t[0]=42
 
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    t[0]=42
TypeError: 'tuple' object does not support item assignment
del t[1]
 
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    del t[1]
TypeError: 'tuple' object doesn't support item deletion
t
 
(52, 23, 'abc')
k=(12,52,85,(5,"abc",5.5.100)
   
SyntaxError: invalid syntax. Perhaps you forgot a comma?
k=(12,52,85,(5,"abc",5.5),100)
   
type(t)
   
<class 'tuple'>
type(k)
   
<class 'tuple'>
k[3]
   
(5, 'abc', 5.5)
k[3][1]
   
'abc'
k[3][1][1]
   
'b'
k[3][1][1][1]
   
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    k[3][1][1][1]
IndexError: string index out of range
k[3][1][2]
   
'c'
t
   
(52, 23, 'abc')
####################################################################
   
s={1,1,2,2,3,4,4,3}
   
type(s)
   
<class 'set'>
print (s)
   
{1, 2, 3, 4}
s[0]
   
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[0:2]
   
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    s[0:2]
TypeError: 'set' object is not subscriptable
s
   
{1, 2, 3, 4}
s2={23,3,41,4}
   
s.intersection(s2)
   
{3, 4}
s.union(s2)
   
{1, 2, 3, 4, 41, 23}
s.add(100)
   
s
   
{1, 2, 3, 100, 4}
s.discard(100)
   
s
   
{1, 2, 3, 4}
s.remove(3)
   
s
   
{1, 2, 4}
s.pop(2)
   
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    s.pop(2)
TypeError: set.pop() takes no arguments (1 given)
s1={44,22,33}
   
s.update(s1)
   
s
   
{1, 2, 33, 4, 44, 22}
s.clear()
   
s
   
set()
#max,min,len
   
