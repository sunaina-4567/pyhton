# class phone :
  
#   def __init__(self, name , ram , rom):
#     self.name = name
#     self.ram  = ram
#     self.rom  = rom

#   def sayHello(self):
#       print(f"hello{self.name}")

#   def getInfo(self):
#         print(f"name:{self.name}, ram:{self.ram}, rom:{self.rom}")

# p1 = phone("phone1",8,500)   
# p2 = phone("phone2" , 16,250)
    
# p1.sayHello()
# p2.sayHello()

# p1.getInfo()
# p2.getInfo()




# class collage:
#     def __init__(self, name , roll):
#         self.name = name
#         self.roll = roll


#     def getinfo(self):
#         print(f"name: {self.name},roll: {self.roll}")    

# s1 = collage("stu1" ,5)    
# s2 = collage("stu2",6)    


# s1.getinfo()
# s2.getinfo()




# class student:
#     def __init__(self , name , age  ,  roll):
#         self.name = name
#         self.roll = roll
#         self.age  = age


#     def getinfo(self):
#         print(f"name: {self.name} , age : {self.age} , roll: {self.roll}")    

# s1 = student("sunaina" , 19 , 56)    
# s2 = student("saniya"  , 18 , 45 )    


# s1.getinfo()
# s2.getinfo()






class student:
    def __init__(self, name , age ,rollno, marks=0):
        self.name = name
        self.age = age 
        self.rollno = rollno
        self.marks = marks

    def getinfo(self):
        print(f"name: {self.name}, age: {self.age}, rollno: {self.rollno}, marks: {self.marks}")

    def getmarks(self):
        print(f"name: {self.name}, marks: {self.marks}")

    def addmarks(self, newmarks):
        self.marks = newmarks 
        

s1 = student("sunaina", 23,12)
s2 = student("saniya", 22, 15)


s1.getinfo()
s2.getinfo()
s1.getmarks()
s1.addmarks(50)
s1.getmarks()













