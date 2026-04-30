print("Simple Calculator - Day 2 🔢")
num1 = float(input("Pehla number daalo: "))
num2 = float(input("Dusra number daalo: "))
op = input("Operation chuno + - * / : ")

if op == "+":
    print("Answer:", num1 + num2)
elif op == "-":
    print("Answer:", num1 - num2)
elif op == "*":
    print("Answer:", num1 * num2)
elif op == "/":
    print("Answer:", num1 / num2)
else:
    print("Galat operation daala tu")
