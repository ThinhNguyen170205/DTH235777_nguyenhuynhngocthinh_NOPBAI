'''
Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
đúng phép toán đã nhập.'''
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
operation = input("Nhập phép toán(+, -, *, /)")
if operation == '+':
    result a + b
    print(f"Kết quả: {a} + {b} = {result}")
elif operation == '-':
    result a - b
    print(f"Kết quả: {a} - {b} = {result}")
elif operation == '*':
    result a * b
    print(f"Kết quả: {a} * {b} = {result}")
elif operation == '/'
    if b != 0
    result a / b
    print(f"Kết quả: {a} / {b} = {result}")
    else:
        print("Không thể chia cho 0")
else:
    print("Phép toán không hợp lệ!")