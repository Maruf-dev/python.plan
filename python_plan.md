blind typing

cmd command => (path) color , dir,  cls, python -V, python --version, cd , exit ,code, mkdir (md) | rd | (rmdir /s (delete with subdirectory)),|rename file.pe file.py|ren (rename file )
type(reads the files), | type nul > index.html (creates file) |
echo print(5*5) > demo.py (writes a code inside the file)
del(delete files), date,|
time => use only as a admin | shutdown /s => 1 min to shutdown (/r | /l ) | shutdown /a => to abort the shutting down
how to run in terminal python file;> python file.py
/help

short cuts;

%temp% / %appdata%

.formats;

errors❤;
syntax error;
name error;
TypeError;
IndentationError;
ValueError;
indexerror;
AttributeError;
Logic error;

<!-- KeyError: Occurs when trying to access a dictionary key that doesn't exist

pythonCopymy_dict = {'a': 1}
my_dict['b']  # KeyError: 'b'

ZeroDivisionError: When attempting to divide by zero

pythonCopy10 / 0  # ZeroDivisionError: division by zero -->

# comment;
""" multi line comment """

ctrl + alt + n = run
<!-- what is variable -->
# correct var names;
myvar = 1;
my_var = 2 #snake_case;
_my_var = 3;
myVar = 4 # camelCase
MYVAR = 5
myvar6 = 6

# wrong var names
$ = 3;
& = 4;
3 = 6;
2myvar = "John";
my var = "John";
my-var = "John" #kebab-case;

# odam = 'Jasur '
# markaz = 'best'
# yosh = 25

# print(f"{odam} {markaz}da o'qiydi yoshi {yosh}da.{odam} keyingi yil {yosh+1} ga kiradi")

<!-- theme: str -->

a = "Hello"
t = "python";
g = "juda";
b = "zo'r";


print(t +" " + g + " " + b);

# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
#  Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y


input();
name = input("name?");
print(name, type(name));

a = 18
print(a,type(a))

data = input() #default  #hint

print(data,type(data))

ctrl + shift + p

num = int(input())
print(num, type(num))

<!-- len -->

a = "Hello, World!"
print(len(a))

a = "Hello, World!"
print(a[1])

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a="string"
print(a.index("r"))

soz = input("Enter a string: ")

index = int(input("Enter a number: "))

print(soz[index])

# ctrl + / > comment

<!-- ///////////// -->

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

b = "hello, world!"
print(b.title()) > H W

b = "hello, world!"
print(b.capitalize())

word = "salom MENING ISMIM teamit"
print(word.swapcase())

b = "HELLO, WORLD!"
print(b.casefold()) => advanced version of lower

a = "Hello, World!"
print(a.strip())

print(a.lstrip())
print(a.rstrip())

a = "Hello, World!"
print(a.replace("H", "J"))

b = "HELLOH, WORLD!"
print(b.count("O"))

a = "Hello, World!"
print(a.split(" "))

% a = "Hello, World!"
% l = list(a)
% print(l)
<!-- list -->

# mylist = ["apple", "banana", "cherry"]

a = ['boom','boom','boom','boom',]
print(a)
print(*a)


# len() > Length > uzunlik
# index
# slicing > kesish

# in > bool > ichida

# txt = "The best things in life are free!"
# print("free" in txt)

#mutable & immutable
# thislist = ["apple", "banana", "cherry"]
# thislist[0:2] = "blackcurrant"
# print(thislist)

# room[0:2] = ["mirror","chair"]

% list methods
qop = ["apple", "banana", "cherry"]
# qop.remove("olcha")
# qop.pop()
# qop.insert(0,"uzum")
# qop.append("false")
# quti.extend(qop)
# del qop[0]
# del qop
# qop.clear()
# qop.sort()
# qop.reverse()

-_-_-_- tuple_-_-_-_-_-
-Tuble listni elementlarini o'zgarimas ko'rinishi sifatida qabul qilish mmkn.

tuple1 = (33,55,66)
tuple1[0] = 88 => type error chunki tuple qismlarini o'zgartirib bo'lmaydi (as a str)


<!-- # Boolean (bool) -->

# true
# false

# >
# <
# ==
# !=
# <=
# >=

# a = 30
# b = 171


# nesting
# if a == b: #true
#     print("a katta b dan")
# else: #false
#     print("demak b katta yoki teng")

# a = input("login...")

# login = "maroof"

# if a != login:
#     print("qayta urining")
# else:
#     print("kiring")

# ⇓
# if a == login
    # print("kiring")

# and & or

<!-- looping -->
# for
# while

#break & continue


<!-- function -->
# def func(a):
    return a
func(13)




<!--local & global libraries  -->

# import time

# nol = 0
# qop = []
# for i in "kompyuter":
#     time.sleep(1)
#     nol+=1
#     qop.append(i)
#     print(nol)
#     print(qop)




# research % problem solving



# isinstance > later