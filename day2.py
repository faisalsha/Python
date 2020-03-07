# def leap_year(year):
#     return year%4==0 and (year % 400==0 or year %100 !=0 )

# print(leap_year(2000))

#prime numbers:
# def prime_num(num):
#     if num >1:
#         for i in range(2,num):
#             if num % i==0:
#                 print(f"The given {num} is not a prime number")
#                 break
#         else:
#             print("its a prime number:")
#     else:
#         print("its not a prime number")
    
    



# prime_num(7)

# #prime numbers in the range from 1,50:
num=1
num2=10
list=[]
for i in range(num,num2+1):
    for j in range(2,i):
        if   i % j == 0:
           break    
    else:
        list.append(i)
       
    
    
for i in list:
    print(i)


# for i in range(2,2):
#     print(i)