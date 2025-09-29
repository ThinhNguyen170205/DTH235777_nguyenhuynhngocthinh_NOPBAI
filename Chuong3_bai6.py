'''
Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm). 
'''
donvi = ["","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
chuc = ["","mười","hai mươi","ba mươi","bốn mươi","năm mươi","sáu mươi","bảy mươi","tám mươi","chín mươi"]
n = int(input("Nhập một số (0-99): "))
if 0 <= n <= 99:
    if n == 0:
        print("Không")
    else
        chuc1 = n // 10
        donvi1 = n % 10
        if chuc1 == 1 and donvi1 == 0:
            print("mười")
        elif chuc1 == 1:
            print("mười{donvi[donvi1]}")
        else
            if donvi1 == 0:
                print("{chuc[chuc1]}")
            else
                print("{chuc[chuc1]}{donvi[donvi1]}")
else:
    print("Số nhập vào không hợp lệ!Vui lòng nhập một số có tối đa 2 chữ số.")
