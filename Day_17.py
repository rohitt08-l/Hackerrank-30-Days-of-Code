#Write your code here
class Calculator:
    def power(self,a,b):
        self.a=a
        self.b=b
        if self.a<0 or self.b <0:
            return "n and p should be non-negative"
        else:
            return a**b
myCalculator=Calculator()
T=int(input("Enter the number of test cases: "))
for i in range(T):
    n,p = map(int, input("Enter two integers separated by a space: ").split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   