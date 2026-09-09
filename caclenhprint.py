# -*- coding: utf-8 -*-
"""

Video lệnh print
"""
# Các loại print
# print không có chủ thể 
print ()
# print có chủ thể ở trong 
print ("hello world")
# print ngăn cách nhau bằng khoảng trắng
print ("hello", "hung", 12)
# print ngăn cách bằng ký tự mình mong muốn bằng sep
print ("hello", "Dao", "Quang","Hung", sep=" ")
print ("hello", "Dao", "Quang","Hung", sep=",")
# kết thúc câu bằng ký tự mình muốn với end
print ('Bạn tên là gì', end=': ')
print ('Đào Quang Hưng')
# nêu kh có end
print ('Bạn tên là gì')
print ('Đào Quang Hưng')
# truyền dữ liệu 
print ('tên bạn={0}, Họ bạn là={1}'.format('hưng','quang'))
#print đi kèm phép tính
print ('Tổng của hai số tự nhiên với nhau là:',3+5)