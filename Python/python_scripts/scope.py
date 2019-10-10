#scopes

a = 100

def f1():
    print(a)

def f2():
    print(a)


# local
a = 250

def f1 ():
    a = 100
    print(a)

def f2 ():
    a = 50
    print(a)

f1()
f2()
print(a)
print(f1()+f2())
