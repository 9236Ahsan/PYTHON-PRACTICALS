def fact(no):
   fact=1
   while (no!=0):
         fact=fact*no
         no=no-1
   print("the factorial of is given below\n",fact)
no=int(input("enter the number for checking the factor is"))
fact(no)