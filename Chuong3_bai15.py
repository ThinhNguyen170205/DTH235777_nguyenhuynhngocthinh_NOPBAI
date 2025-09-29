'''
Giải thích cách chạy các dòng lệnh range
(a) range(5)
(b) range(5, 10)
(c) range(5, 20, 3)
(d) range(20, 5, -1)
(e) range(20, 5, -3)
(f) range(10, 5)
(g) range(0)
(h) range(10, 101, 10)
(i) range(10, -1, -1)
(j) range(-3, 4)
(k) range(0, 10, 1)
'''
(a)start = 0, stop = 5, step = 1
Kết quả: [0, 1, 2, 3, 4]
(b)Bắt đầu từ 5 đến trước 10, bước nhảy 1
Kết quả: [5, 6, 7, 8, 9]
(c)Bắt đầu từ 5, tăng dần mỗi lần 3 đơn vị, đến trước 20
Kết quả: [5, 8, 11, 14, 17]
(d)Bắt đầu từ 20, giảm dần mỗi lần 1 đơn vị, dừng trước 5
Kết quả: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
(e)Bắt đầu từ 20, giảm mỗi lần 3 đơn vị, dừng trước 5
Kết quả: [20, 17, 14, 11, 8]
(f)Mặc định step = 1, nhưng start > stop -> không hợp lệ
Kết quả: [] (range rỗng)
(g)Tức là range(0, 0) -> không có giá trị nào
Kết quả: [] (rỗng)
(h)Bắt đầu từ 10, tăng mỗi lần 10 đơn vị, đến trước hoặc bằng 100
Kết quả: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
(i)Bắt đầu từ 10, giảm dần mỗi lần 1, dừng trước -1
Kết quả: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
(j)Bắt đầu từ -3, tăng mỗi lần 1, đến trước 4
Kết quả: [-3, -2, -1, 0, 1, 2, 3]
(k)Bắt đầu từ 0, tăng mỗi lần 1, đến trước 10
Kết quả: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]