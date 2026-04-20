# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    else :
        return True
for i in range(n):
    a=int(input())
    if is_prime(a)==True:
        print("Prime")
    else:
        print("Not prime")
