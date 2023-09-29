class Calculator:
    #Addition
    def add(self, *args):
        return sum(args)

    #Subtraction
    def subtract(self, *args):
        return args[0] - sum(args[1:])
    
    #Multiplication
    def multiply(self, *args):
        product = 1
        for i in args:
            product *= i
        return product
    
    #Division *
    def divide(self, *args): 
        if 0 in args[1:]:
            return None, "Division by Zero"
        quotient = args[0]
        for q in args[1:]:
            quotient /= q
        return quotient
    
    #Exponent
    def exponentiate(self, a, b):
        return a ** b
