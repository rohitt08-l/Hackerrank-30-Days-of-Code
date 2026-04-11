class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        pass
        divs = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divs.append(i)
                if i != n//i:
                    divs.append(n//i)
        #print(sum(divs)-n)
        return sum(divs)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
<<<<<<< HEAD
print(s)
=======
print(s)
>>>>>>> cfc6c7f030cc49b950ef0dfba8b3274aaab7723e
