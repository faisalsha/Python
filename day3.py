#factorial of a given number:
# def fact(num):
#     fact=1
#     if num <0:
#         print("factorial doesnt mnot exist")
#     elif num ==0:
#         print("factorial is 1")
#     else:
#         for i in range(1,num+1):
#             fact=fact*i
#         print(f"factorial of {num} is {fact}")


# fact(5)

#Factorial using recursion
# def Recurion(num):
#     if num < 0:
#         print(f"factorial doest exist for {num}")
#     elif num ==1:
#         return  num
#     else:
#         return num*Recurion(num-1)
# num=5
# print(f"the factorial of {num} is {Recurion(num)}")

#find teh factors of 13 from the list:
# def Factors(list):
#     lis=[]
#     for i in list:
#         if i %13 ==0:
#             lis.append(i)
#         else:
#             pass
    
#     for i in lis:
#         print(i,end=" ")


# list=[12, 65, 54, 39, 102, 339, 221]
# Factors(list)

#sum of all natural nubers
# n=5
# if n < 0:
#     print("enter a pos number")
# else:

#     # sum=0
#     # while num > 0:
#     #     sum=sum+num
#     #     num =num-1
#     sum=n*(n+1)/2
#     print(f"sum is {sum}")
#Power of 2:
# def is_power_of_two(n):
#     """Return True if n is a power of two."""
#     if n <= 0:
#         return False
#     else:
#         return n & (n - 1) == 0
# n=int(input("enter the number:"))
# if  is_power_of_two(n):
#     print(f"{n} is a power of 2")
# else:
#     print(f"{n} is  not a power of 2")

# def _is_a_power_of_two(num):
#     if num <0:
#         print("its not a power of 2")
#     else:
#         while num !=1:
#             if num %2 ==0:
#                 num=num //2
#             else:
#                 return False
#         return True
# num=6
# if _is_a_power_of_two(num):
#     print(f"{num} is a power of 2")
# else:
#      print(f"{num} is  not a power of 2")


#Mutiplication Tables
# def Tables(num):
#     for i in range(1,11):
#         print(f"{num} X {i} = {num * i}")


# Tables(7)

#Removing Punchuation from strings
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

new_str=""
for i in my_str:
    if i not in punctuations:
        new_str=new_str+i

print(new_str)