user = input("Expression: ")
expression = user.split(" ")
x = int(expression[0])
y = (expression[1])
z = int(expression[2])

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z

print(float(result))

