class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        b=max(a)
        c=min(a)
        self.maximumDifference=abs(b-c)
	# Add your code here

# End of Difference class

_ = input("Enter the number of elements: ")
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print("Maximum Difference:", d.maximumDifference)