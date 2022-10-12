Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={"name":["mahak","mayuri","kejal"]"semester":[2,1,2]}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d1={"name":["mahak","mayuri","kejal"],"semester":[2,1,2]}
print(d1)
{'name': ['mahak', 'mayuri', 'kejal'], 'semester': [2, 1, 2]}
d["name"]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d["name"]
NameError: name 'd' is not defined. Did you mean: 'd1'?
d["name"]+=["bunny"]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d["name"]+=["bunny"]
NameError: name 'd' is not defined. Did you mean: 'd1'?
d1["name"]+=["bunny"]
print(d1)
{'name': ['mahak', 'mayuri', 'kejal', 'bunny'], 'semester': [2, 1, 2]}
d1["name"]+="bunny"
print(d1)
{'name': ['mahak', 'mayuri', 'kejal', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1["name"]+=["hello"]
print(d1)
{'name': ['mahak', 'mayuri', 'kejal', 'bunny', 'b', 'u', 'n', 'n', 'y', 'hello'], 'semester': [2, 1, 2]}
d1["semester"]+=["3rd"]
print[d1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print[d1]
TypeError: 'builtin_function_or_method' object is not subscriptable
d1["semester"]+=[3]
print(d1)
{'name': ['mahak', 'mayuri', 'kejal', 'bunny', 'b', 'u', 'n', 'n', 'y', 'hello'], 'semester': [2, 1, 2, '3rd', 3]}
d1["name"]+=["hiiii"]
print(d1)
{'name': ['mahak', 'mayuri', 'kejal', 'bunny', 'b', 'u', 'n', 'n', 'y', 'hello', 'hiiii'], 'semester': [2, 1, 2, '3rd', 3]}
d1["name"].insert(1,"hellloooooo")
d1
{'name': ['mahak', 'hellloooooo', 'mayuri', 'kejal', 'bunny', 'b', 'u', 'n', 'n', 'y', 'hello', 'hiiii'], 'semester': [2, 1, 2, '3rd', 3]}
d1["sem"]=d1.pop("semester")
d1
{'name': ['mahak', 'hellloooooo', 'mayuri', 'kejal', 'bunny', 'b', 'u', 'n', 'n', 'y', 'hello', 'hiiii'], 'sem': [2, 1, 2, '3rd', 3]}
#f-string/string format
a="mahak"
b="upflairs"
f"hi{a} welcome to {b}"
'himahak welcome to upflairs'
f"hi {a} welcome to {b}"
'hi mahak welcome to upflairs'
f"hi {b} welcome to {a}"
'hi upflairs welcome to mahak'
"hi {} welcome to {}".format("mahak","upflairs")
'hi mahak welcome to upflairs'
for i in[1,2,3,4,5]:
    print(i)
for i in [1,2,3,4,5]:
    print(i)
    
SyntaxError: invalid syntax
for i in [1,2,3,4,5]:
    print(i)
for i in ("a","b","c","d"):
    
SyntaxError: invalid syntax
for i in [1,2,3,4,5]:
    print(i)

    
1
2
3
4
5


for i in ("a","b","c","d"):
    print(i)

    
a
b
c
d
for i in "helloworld"
SyntaxError: expected ':'
for i in "helloworld":
    print(i)

    
h
e
l
l
o
w
o
r
l
d
for i in "helloworld":
    print("hello
          
SyntaxError: unterminated string literal (detected at line 2)
for i in "helloworld":
    print("helloworld")

          
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
for x in "helloworld":
          print(x)

          
h
e
l
l
o
w
o
r
l
d
for x in "helloworld":
          print("helloworld")

          
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
helloworld
for x in "helloworld":
          print(x)
          print("hello")

          
h
hello
e
hello
l
hello
l
hello
o
hello
w
hello
o
hello
r
hello
l
hello
d
hello
print("hello")
          
hello
print(x)
          
d
for x in "hello":
          print(x)
          print("hello")
          print("helloworld")

          
h
hello
helloworld
e
hello
helloworld
l
hello
helloworld
l
hello
helloworld
o
hello
helloworld
