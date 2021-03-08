# Given two numbers, represented as strings, multiply them and return as string
# Rules: CANNOT directly convert string to int using built in methods
def parse_number(self, num):
    result = 0
    for i in range(1, len(num) + 1):
        char = num[-i]
        if char == '9':
            multiplier = 9
        elif char == '8':
            multiplier = 8
        elif char == '7':
            multiplier = 7
        elif char == '6':
            multiplier = 6
        elif char == '5':
            multiplier = 5
        elif char == '4':
            multiplier = 4
        elif char == '3':
            multiplier = 3
        elif char == '2':
            multiplier = 2
        elif char == '1':
            multiplier = 1
        elif char == '0':
            multiplier = 0
        result += multiplier * 10 ** (i-1)
    return result

def multiply(self, num1: str, num2: str) -> str:
    return str(self.parse_number(num1) * self.parse_number(num2))
