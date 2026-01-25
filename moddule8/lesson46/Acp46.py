class Expression:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self):
        return (self.a + self.b) * self.c


# Create object
exp = Expression(2, 3, 4)

# Call method and print result
result = exp.evaluate()
print("Result of the expression is:", result)
