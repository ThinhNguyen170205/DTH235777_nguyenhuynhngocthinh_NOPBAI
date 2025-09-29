'''
 Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
 '''
 month = int(input("Nhập vào tháng(1-12): "))
 if month == 1 or month == 2 or month == 3:
    quarter = 1
elif month == 4 or month == 5 or month == 6:
    quarter = 2
elif month == 7 or month == 8 or month == 9:
    quarter = 3
elif month == 10 or month == 11 or month == 12:
    quarter = 4
else:
    quarter = None
    print("Tháng nhập vào không hợp lệ!")
if quarter is not None:
    print("Tháng {month} thuộc quý {quarter} trong năm.")
     
