# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:15:24 2026

@author: Hung
"""
""" Học trên trường buổi 1 """
# trước input phải thêm định dạng kiểu dữ liệu để lệnh print xác định kiểu dữ liệu in ra
a= float(input('Điểm quá trình của bạn: '))
b= float(input('Điểm thi của bạn:'))
d= float(input('Tỷ lệ điểm quá trình:'))
c= a* (d/100) +b* ((100-d)/100)
# f= float làm tròn chữ số thập phân thứ 2
print=(f'Điểm kết thúc học phần của bạn:{round(c, 2)}')
