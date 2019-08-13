def minposition(A, num):
   minposition = A.index(min(A))
   print (minposition + 1)
A=list()
num=int(input())
for i in range(int(num)):
   k=int(input(""))
   A.append(k)
minposition(A,num)
