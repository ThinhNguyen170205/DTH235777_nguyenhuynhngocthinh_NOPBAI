'''Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày
vừa nhập (ngày/tháng/năm).'''
from datetime import datetime, time1
date_input = input("Nhập vào một ngày(ngày/tháng/năm): ")
date_obj = datetime.strptime(date_input, "%d/%m/%y")
next_day = date_obj + time1(days = 1)
print("Ngày kế tiếp là:", next_day.strftime("%d/%m/%y"))