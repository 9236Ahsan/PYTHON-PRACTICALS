o=open("apple.txt")
n=int(input("enter the limit for getting the lines\n"))
for i in range(n):
    print(o.readline())
