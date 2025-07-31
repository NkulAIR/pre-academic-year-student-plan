import operator

user = (input("Expression:")).strip(" ")
expression = user.split(" ")
x = int(expression[0])
y = (expression[1])
z = int(expression[2])

if y == "+":
    result = operator.add(x, z)
    print(float(result))
elif y == "-":
    result = operator.sub(x, z)
    print(float(result))
elif y == "*":
    result = operator.mul(x, z)
    print(float(result))
elif y == "/":
    result = operator.truediv(x, z)
    print(float(result))




