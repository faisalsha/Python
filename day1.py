# # # # # #sample Input
# # # # # 1
# # # # # 1
# # # # # 1
# # # # # 2

# # # # # #SAMPLE oUTPUT
# # # # # #[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# # # # # #x=1
# # # # # x = int ( input())  

# # # # # #y=1
# # # # # y = int ( input())

# # # # # #Z=1
# # # # # z = int ( input())

# # # # # #n=1
# # # # # n = int ( input()) 

# # # # # ar = [] 
# # # # # p = 0 
# # # # # for i in range ( x + 1 ) :
# # # # #      for j in range( y + 1):
# # # # #          for k in range(z+1):
# # # # #             if i+j+k != n:
# # # # #                 ar.append([])
# # # # #                 ar[p] = [ i , j , k ] 
# # # # #                 p+=1 
# # # # # print (ar)
# # # # # print(ar[2])




# # # # #Question 2:
# # # # #Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# # # # #The first line contains n. The second line contains an array A[]  of  n nintegers each separated by a space


# # # # players=int(input("enter the number of players:"))
# # # # list=[]
# # # # for i in range(1,players+1):
# # # #     scores=int(input(f"enter player {i} score"))
# # # #     list.append(scores)

# # # # list.sort()
# # # # print(list)
# # # # list.pop()
# # # # print(list)
# # # # # print(a)
# # # # print(f"The runner up is {list[-2]}")



# # # #Question3 :
# # # # Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# # # # Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.



# # # numOfStudents=input()
# # # studentAndMarks = [[input(),input()] for i in range(int(numOfStudents))]
# # # print(studentAndMarks)

# # # marks=[]
# # # for i in range(int(numOfStudents)):
# # #     marks.append(float(studentAndMarks[i][1]))
    
# # # # print(marks)

# # # smallest=secondSmallest=max(marks)
# # # for i in range(int(numOfStudents)):
# # #     if(marks[i]<smallest):
# # #         secondSmallest=smallest
# # #         smallest=marks[i]
# # #     else:
# # #         if(marks[i]<secondSmallest and marks[i]!=smallest):
# # #             secondSmallest=marks[i]
# # # print(smallest)
# # # print(secondSmallest)


# # #Multiplication table:

# # num = int(input("Enter the number: "))

# # # print("Multiplication Table of", num)
# # # for i in range(1, 11):
# # # #    print(num,"X",i,"=",num * i)
# # #    print(f"{num} X {i} = {num *i }")


# # arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
# # for k in arr:
# #    print(k,end=" ")


# dist={
#    0:2,
#    1:2,
#    2:2
# }

# n_list=dist.keys()
# print(n_list)
# for i in n_list:
#    for j in n_list:
#       if j >= j+1:
#          temp=i
#          i=i+1
#          j+1=temp
#       else:
#          pass

# for i in n_list:
#    print(str(dist[i])*i)

num=[0,2,1,0,1,2]
d={ }
for i in num:
   if i not in d:
      d[i]=1
   elif i in d:
      d[i]=d[i]+1

print(d)
s=set(d)
s=list(s)
print(s)
for i in s:
   if i in d.keys():
      print(str(i)*d[i],end="")
print()
# for i in s:
#    for j in range(len(s)):
#       if i >i+1:
#          temp=s[i]
#          s[i]=s[i+1]
#          s[i+1]=temp

# print(s)