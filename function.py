def info():
    print("hello")
info()
info()
info()
info()
info()

def great (name):
    print(f"happy birthday { name}")
great("sunaina")  
great("saniyaa")
great("nishu")
great("kamni")


def info(name,city,age):
    print(f"hello { name},from {city}. you're {age} years old")
info ("saniya", "joya", 18)
info("sunaina", "kailsa", 19)   
info("nishu", "mandhiuy" , 20)
info("kamni", "mbd", 18) 

def studentinfo( name , marks , collage ="SSGT"):
    print(f" hello { name}, your marks {marks}. from {collage}")
studentinfo("sunaina", 500, "satya" )
studentinfo("saniya", 600, "iftm")
studentinfo("nishu", 300,"tmu"  )
studentinfo("kamni", 400 )  

def add(a,b):
    return a+b
print(add(4,5))

def sub(a,b):
    print(a-b)
sub(4,5)    