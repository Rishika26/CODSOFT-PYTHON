num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("Enter + for addition, - for subtraction, * for multiplication, / for division and % for modulus")
op = input("Enter desired operation : ")
match op:
    case "+" :
        print(num1+num2)

    case "-" :
        print(num1-num2)

    case "*" :
        print(num1 * num2)

    case "/" :
        print(num1 / num2)

    case "%" :
        print(num1 % num2)

    case _ :
        print ("Invalid operation")