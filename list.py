number = [ 1,2,3,4,5]
fruits= [ " apple ", "mango", "orange"]
mixed= [ 23, " sunaina", 4.6]
print(number)
print(fruits)
print(mixed)
print(fruits[2])
fruits[2]= "mango"
print(fruits)

nums=[1,2,3,4,5,]
print(nums)

nums2 =[]
for n in nums2:
    nums2.append(n+9)
print(nums2) 
   

nums=[]
for n in range(1,8):
   nums.append(n)
print(nums)   

from functools import reduce 

nums= [1,2,3,4,5,6,7,8,9,10]
res = reduce(lambda x,y : x+y, nums)
print(res)


nums=[1,2,3,4,5]
def abc(x):
    return x*x
res = list(map(abc,nums))
res = list(map(lambda x: x*x , nums))
print(res)


nums = [1,2,3,4,5,6]
res = list(filter(lambda x: x>3, nums))
print(res)