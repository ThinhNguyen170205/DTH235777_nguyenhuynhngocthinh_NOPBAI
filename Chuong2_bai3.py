'''
Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra
điểm trung bình của học sinh đó với hai số lẻ thập phân.
'''
toan=float(input("Nhập điểm Toán:"))
ly=float(input("Nhập điểm lý:"))
hoa=float(input("Nhập điểm hóa:"))
dtb=(toan+ly+hoa)/3
print("Điểm trung bình=",dtb)
print("Điểm trung bình=",round(dtb,2))
'''
Cách 2:
print("Chương trình tính điểm trung bình")
toan,ly,hoa=eval(input("Nhập điểm toán,lý,hóa:"))
print("Điểm toán=",toan)
print("Điểm lý=",ly)
print("Điểm hóa=",hoa)
dtb=(toan+ly+hoa)/3
print("Điểm trung bình=",dtb)
print("Điểm làm tròn=",round(dtb,2))
'''
