import random

class Encryptor:
    def __init__(self, num1, num2):
        self.__num1 = num1  
        self.__num2 = num2
        self.__operation = random.choice(["+", "-", "*", "/"])  

    def __calculate(self):
        231
        if self.__operation == "+":
            return self.__num1 + self.__num2
        elif self.__operation == "-":
            return self.__num1 - self.__num2
        elif self.__operation == "*":
            return self.__num1 * self.__num2
        elif self.__operation == "/" and self.__num2 != 0:
            return self.__num1 / self.__num2
        else:
            return "Invalid operation"

    def __str__(self):
       
        return f"Result: {self.__calculate()} (Operation: {self.__operation})"


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


enc = Encryptor(num1, num2)


print(enc)
