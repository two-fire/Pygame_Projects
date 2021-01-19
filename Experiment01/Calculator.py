# Create a script that accepts 2 numbers and an operator (+, -, *, /), and prints the result of the operation.
# 创建一个脚本，该脚本接受2个数字和操作符(+，-，*，/)，并打印操作结果
def culculate(n1, n2, o):
    if o == "+":
        res = n1 + n2
    elif o == '-':
        res = n1 - n2
    elif o == '*':
        res = n1 * n2
    elif o == '/':
        if n2 == 0:
            print("除数不可为0")
        else:
            res = n1 / n2
    return res

print("请输入两个数字和操作符(+，-，*，/)：")
num1 = int(input("数字1："))
num2 = int(input("数字2："))
operator = input("操作符：")
res = culculate(num1, num2, operator)
print(num1,operator,num2," = ",res)
