def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)
print(factorial(5))

def rec_sum (n):
    if n==0: 
      return 0
    return(n % 10 )+ rec_sum(n // 10)
print(rec_sum(1234))