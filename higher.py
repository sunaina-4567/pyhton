def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul (a,b):
    return a*b
def div(a,b):
    return a/b

def calc(fn, a,b):
    return fn(a,b)

print (calc(sum,5,6))
print(calc(sub, 5,8))
print (calc(mul , 4,4))
print(calc(div ,25, 5))


