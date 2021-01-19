# Write a script that will ask for the sides of a rectangular and print out the area.
# Provide error messages if either of the sides is negative.
# 编写脚本，询问矩形的边并打印出该区域。 如果任何一方为负，则提供错误消息。

def print_rectangular(x, y):
    for i in range(x):
        print("+", end=" ")
    print()
    width = y - 2
    lenth = x - 2
    for i in range(width):
        print("+", end=" ")
        for j in range(lenth):
            print(" ", end=" ")
        print("+")
    for i in range(x):
        print("+", end=" ")

def print_area(x, y):
    print("\n矩形的面积为：", x * y)

print("请输入矩形的边长")
x = int(input("矩形的长："))
y = int(input("矩形的宽："))
print("打印出该矩形：")
if x <= 0 | y < 0:
    print("边长不能为负")
print_rectangular(x, y)
print_area(x, y)