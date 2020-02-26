""" remainder= lambda num: num % 2 

print(remainder (5)) 
#remainder is defined as a function, here it e

product = lambda x,y: x * y
######### argument : expression 
print(product(2,3))
### higher calling function : a function that calls another function 

def  testfunc(num):
    return lambda x: x*num

result1 = testfunc(10)

print( result1 (9))
#### the argument is multiplying by a unknown number (num)
### result 1 is a function that we are calling, so 10 becomes num and 9 is x  
result2 = testfunc(1000)
print( result2 (9)) """

def myfunc(n):
    return lambda a: a*n 

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler (11))
print(mytripler(11))

num_list= [2,6,8,10,11,4,12,7,13,0,2]

filtered_list= list(filter(lambda num: (num >7), num_list))
### this applies the filter function the list above, so every number in the list is compared to 7
print(filtered_list)

mapped_list = list(map(lambda num: num % 2, num_list ))
print(mapped_list)