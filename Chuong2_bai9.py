'''
Cho các biến với giá trị
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5
Cho biết kết quả và giải thích cách thực hiện của các lệnh sau:
(a) i1 + (i2 * i3)
(b) i1 * (i2 + i3)
(c) i1 / (i2 + i3)
(d) i1 // (i2 + i3)
(e) i1 / i2 + i3
(f) i1 // i2 + i3
(g) 3 + 4 + 5 / 3
(h) 3 + 4 + 5 // 3
(i) (3 + 4 + 5) / 3
(j) (3 + 4 + 5) // 3
(k) d1 + (d2 * d3)
(l) d1 + d2 * d3
(m) d1 / d2 - d3
(n) d1 / (d2 - d3)
(o) d1 + d2 + d3 / 3
(p) (d1 + d2 + d3) / 3
(q) d1 + d2 + (d3 / 3)
(r) 3 * (d1 + d2) * (d1 - d3)
'''
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5
print("(a)", i1 + (i2 * i3)) = -13 # Tính phép nhân trong dấu ngoặc: i2 * i3 = 5 * (-3) = -15, Cộng i1 với kết quả: 2 + (-15) = -13
print("(b)", i1 * (i2 + i3)) = 4 # Tính trong ngoặc: i2 + i3 = 5 + (-3) = 2, Nhân i1 với kết quả: 2 * 2 = 4
print("(c)", i1 / (i2 + i3)) = 1.0 # Tính trong ngoặc: i2 + i3 = 2, Chia i1 cho kết quả: 2 / 2 = 1.0
print("(d)", i1 // (i2 + i3)) = 1 # Tính trong ngoặc: 2, Chia lấy phần nguyên: 2 // 2 = 1
print("(e)", i1 / i2 + i3) = -2.6 # Thực hiện phép chia trước: 2 / 5 = 0.4, Cộng với i3: 0.4 + (-3) = -2.6
print("(f)", i1 // i2 + i3) = -3 # Chia lấy phần nguyên: 2 // 5 = 0, Cộng với i3: 0 + (-3) = -3
print("(g)", 3 + 4 + 5 / 3)  = 9.6668 # Phép chia được ưu tiên: 5 / 3 ≈ 1.6667, Cộng tuần tự: 3 + 4 = 7, Cộng tiếp: 7 + 1.6667 = 8.6667
print("(h)", 3 + 4 + 5 // 3)  = 8 # Phép chia lấy phần nguyên: 5 // 3 = 1, Cộng tuần tự: 3 + 4 = 7, Cộng tiếp: 7 + 1 = 8
print("(i)", (3 + 4 + 5) / 3) = 4.0 # Tính tổng trong ngoặc: 3 + 4 + 5 = 12, Chia cho 3: 12 / 3 = 4.0
print("(j)", (3 + 4 + 5) // 3) = 4 # Tính tổng: 12, Chia lấy phần nguyên: 12 // 3 = 4
print("(k)", d1 + (d2 * d3)) = -0.5 # Nhân trong ngoặc: 5.0 * -0.5 = -2.5, Cộng 2.0 + (-2.5) = -0.5
print("(l)", d1 + d2 * d3) = -0.5 # 
print("(m)", d1 / d2 - d3) = 0.9 # Chia: 2.0 / 5.0 = 0.4, Trừ một số âm bằng cộng: 0.4 - (-0.5) = 0.4 + 0.5 = 0.9
print("(n)", d1 / (d2 - d3)) = 0.363636 # Tính trong ngoặc: 5.0 - (-0.5) = 5.5, Chia: 2.0 / 5.5 ≈ 0.3636
print("(o)", d1 + d2 + d3 / 3) = 6.8333 # -0.5 / 3 ≈ -0.1667, Cộng: 2.0 + 5.0 = 7.0, Cộng tiếp: 7.0 + (-0.1667) ≈ 6.8333
print("(p)", (d1 + d2 + d3) / 3) = 2.1666 # Tính tổng: 2.0 + 5.0 + (-0.5) = 6.5 , Chia: 6.5 / 3 ≈ 2.1667
print("(q)", d1 + d2 + (d3 / 3)) = 6.8333 # 
print("(r)", 3 * (d1 + d2) * (d1 - d3)) = 52.5 # Tính trong ngoặc đầu: 2.0 + 5.0 = 7.0, Tính trong ngoặc thứ hai: 2.0 - (-0.5) = 2.5, Nhân liên tiếp: 3 * 7.0 = 21.0, Nhân tiếp: 21.0 * 2.5 = 52.5