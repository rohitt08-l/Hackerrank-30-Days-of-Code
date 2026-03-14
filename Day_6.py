# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input("Enter number of test cases: ").strip())

for i in range(T):
    s=input("Enter a string: ").strip()
    even=""
    odd=""
    for i in range(len(s)):
        if i%2==0:
            even=even+s[i]
        else:
            odd=odd+s[i]
    print(even , odd)
