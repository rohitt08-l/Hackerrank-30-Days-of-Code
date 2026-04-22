# Enter your code here. Read input from STDIN. Print output to STDOUT
d1,m1,y1 = map(int,input().split())
d2,m2,y2=  map(int,input().split())
Fine=None
if y1>y2:
    Fine=10000
elif y2==y1 and m1>m2:
    Fine=500*(m1-m2)
elif y2==y1 and m2==m1 and d1>d2:
    Fine=15*(d1-d2)
else:
    Fine=0
print(Fine)
