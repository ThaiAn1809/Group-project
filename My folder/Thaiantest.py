class Calculator:
    def add(self, *arg):
        return sum(arg)




calculator = Calculator()

# Using the different overloaded add methods
sum1 = calculator.add(2, 3)
sum2 = calculator.add(2, 3, 4)
sum3 = calculator.add(2, 3, 4, 5)

print("Sum1:", sum1)
print("Sum2:", sum2)
print("Sum3:", sum3)