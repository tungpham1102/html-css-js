# Bài 01:
#
# Câu hỏi :
# ​Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
# nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

# lis = []
# for i in range(2000, 3201):
#     if i%7==0 and i%5 !=0:
#         lis.append(str(i))
# print(lis)
# print(', '.join(lis))

##################################################################################################
# Bài 02 :
#
# Câu hỏi :
# ​Viết một chương trình có thể tính giai thừa của một số cho trước.
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# k = int(input('nhap k: '))
# giaithua = 1
# if k <= 0:
#     print(giaithua)
# else:
#     for i in range(1, k+1):
#         giaithua *= i
# print(giaithua)
#
# x=int(input("Nhập số cần tính giai thừa:"))
# def fact(x):
#     if x == 0:
#       return 1
#     return x * fact(x - 1)
# print (fact(x))

##################################################################################################
# Bài 03 :
#
# Câu hỏi :
#  Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary
# chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
# Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

# k = int(input('nhap k: '))
# res = dict()
# for i in range(1,k+1):
#     res[i]=i**2
# print(res)

##################################################################################################
# Bài 04:
#
# Câu hỏi :
# ​
#
# Viết chương trình chấp nhận một chuỗi số,
# phân tách bằng dấu phẩy từ giao diện điều khiển,
# tạo ra một danh sách và một tuple chứa mọi số.
#
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# vals = input('nhap val: ')
# lis = []
# tup = tuple()
# for i in vals.split(','):
#     lis.append(i)
#     tup=tuple(lis)
# print(lis)
# print(tup)

# values=input("Nhập vào các giá trị:")
# l=values.split(",")
# t=tuple(l)
# print (l)
# print (t)

##################################################################################################
# Bài 05:
#
# Câu hỏi :
# ​
# Định nghĩa một class có ít nhất 2 method:
#
# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
#
# printString: in chuỗi vừa nhập sang chữ hoa.
#
# Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
#
# Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

# class Handle():
#     def __init__(self):
#         self.str = ''
#     def getString(self):
#         self.str = input('nhap str: ')
#     def printString(self):
#         print(self.str.upper())
#
# str = Handle()
# str.getString()
# str.printString()

# class Handle():
#     def __init__(self):
#         pass
#     def getString(self):
#         str = input('nhap str: ')
#         return str
#     def printString(self):
#         print(self.getString().upper())
#
# str = Handle()
# str.printString()

##################################################################################################
# Bài 06:
#
# Câu hỏi :
# ​Viết một method tính giá trị bình phương của một số.
#
# x = int(input('x = '))
# def square(x):
#     return x**2
#
# print(square(x))

##################################################################################################
# Bài 09:
#
# Câu hỏi :
# ​
#
# Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H])
# (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
# Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng,
#  các giá trị của D được phân cách bằng dấu phẩy.
#
# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

# import math
# D = input('nhap D: ')
# C = 50
# H = 30
# lis = []
# def res(D):
#     for i in D.split(','):
#         q = math.sqrt((2*C*float(i))/H)
#         lis.append(str(int(round(q))))
#     print(','.join(lis))
# res(D)

##################################################################################################
# Bài 10:
#
# Câu hỏi :
# ​
#
# Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
#
# Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
#
# Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# input_str = input('Nhap X, Y: ')
# dimentions = [int(x) for x in input_str.split(',')]
# rowNum = dimentions[0]
# colNum = dimentions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col] = row*col
# print(multilist)

##################################################################################################
# Bài 11:
#
# Câu hỏi :
# Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào,
# phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái,
# phân tách nhau bằng dấu phẩy.
#
# Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.

# input_str = input('str: ')
# item = input_str.split(',')
# print(','.join(sorted(item))+'.')

# items=[x for x in input("Nhập một chuỗi: ").split(',')]
# items.sort()
# print (','.join(items))

##################################################################################################
# Bài 12:
#
# Câu hỏi :
# Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào,
# chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:
#
# Hello world
# Practice makes perfect
#
# Thì đầu ra sẽ là:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT

# input_str = input("Input str: ")
# print(input_str.upper())

# lines = []
# while True:
#    s = input()
#    if s:
#       lines.append(s.upper())
#    else:
#       break
# for sentence in lines:
#     print (sentence)

##################################################################################################
# Bài 13:
#
# Câu hỏi :
# ​
#
# Viết một chương trình chấp nhận đầu vào là
# một chuỗi các từ tách biệt bởi khoảng trắng,
# loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
#
# Giả sử đầu vào là: hello world and practice makes perfect and hello world again

# Thì đầu ra là: again and hello makes perfect practice world

# input_str = input("INput str: ")
# items = [x for x in input_str.split(' ')]
# print(' '.join(sorted(list(set(items)))))

##################################################################################################
# Bài 14:
#
# Câu hỏi :
# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số,
# phân tách bởi dấu phẩy,
# kiểm tra xem chúng có chia hết cho 5 không.
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
#
# Ví dụ đầu vào là: 0100,0011,1010,1001
#
# Đầu ra sẽ là: 1010

# input_num = input("input: ")
# nums = [num for num in input_num.split(",")]
# res = []
# for num in nums:
#     if int(num) % 5 ==0:
#         res.append(num)
# print(', '.join(res))

##################################################################################################
# Bài 15:
#
# Câu hỏi :
# ​Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho
# tất cả các chữ số trong số đó là số chẵn.
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

# lis = []
# for num in range(1000,3001):
#     a = int(num/1000)
#     b = num%1000
#     c = b%100
#     d = c%10
#     tong = int(a)+ int(b/100) + int(c/10)+d
#     if tong % 2 == 0:
#         lis.append(str(num))
# print(', '.join(lis))

# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print (",".join(values))

##################################################################################################
# Bài 16:
#
# Câu hỏi :
# Viết một chương trình chấp nhận đầu vào là một câu,
# đếm số chữ cái và chữ số trong câu đó.
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
#
# Thì đầu ra sẽ là:
#
# Số chữ cái là: 10
# Số chữ số là: 3

# input_str = input('nhap chuoi: ')
# d = {'D':0, "C":0}
# for c in input_str:
#     if c.isalpha():
#         d["C"]+=1
#     elif c.isdigit():
#         d["D"]+=1
#     else:
#         pass
# print(d)

##################################################################################################
# Bài 17:
#
# Câu hỏi :
# Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
#
# Giả sử đầu vào là: Quản Trị Mạng
#
# Thì đầu ra là:
#
# Chữ hoa: 3
#
# Chữ thường: 8

# input_str = input("nhap : ")
# result = {"U":0, "L":0}
# for char in input_str:
#     if char.isupper():
#         result["U"]+=1
#     elif char.islower():
#         result["L"]+=1
#     else:
#         pass
# print(result)
# print(result["U"])

##################################################################################################
# Bài 18:
#
# Câu hỏi:
# Viết một chương trình tính giá trị của a + aa + aaa + aaaa với
# a là số được nhập vào bởi người dùng.
#
# Giả sử
# a được nhập vào là 1 thì đầu ra sẽ là: 1234
#
# n = int(input("nhap n: "))
# result = n*1000+2*n*100+3*n*10+4*n
# print(result)

##################################################################################################
# Bài 20:
#
# Câu hỏi :
#  Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
#
# Định dạng nhật ký được hiển thị như sau:
#
# D 100
# W 200
#
# (D là tiền gửi, W là tiền rút ra).
#
# Giả sử đầu vào được cung cấp là:
#
# D 300
#
# D 300
#
# W 200
#
# D 100
#
# Thì đầu ra sẽ là:
#
# 500

# import sys
# netAmount = 0
# # Bài tập Python 20, Code by Quantrimang.com
# while True:
#     s = input("Nhập nhật ký giao dịch: ")
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#          netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print (netAmount)

##################################################################################################
# Bài 21:
#
# Câu hỏi :
# Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký.
# Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
#
# Các tiêu chí kiểm tra mật khẩu bao gồm:
#
# 1. Ít nhất 1 chữ cái nằm trong [a-z]
# 2. Ít nhất 1 số nằm trong [0-9]
# 3. Ít nhất 1 kí tự nằm trong [A-Z]
# 4. Ít nhất 1 ký tự nằm trong [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12
#
# Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và
# kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không.
#     Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.
#
# Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345
#
# Thì đầu ra sẽ là: ABd1234@1

# import re
# value = []
# items = [x for x in input("Nhap mat khau: ").split(",")]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(", ".join(value))

##################################################################################################
# Bài 22:
# Câu hỏi: Viết chương trình sắp xếp tuple(name, age, score)
# theo thứ tự tăng dần, name là string, age và height là number.
# Tuple được nhập vào bởi người dùng.Tiêu chí sắp xếp là:
# Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score.
# Ưu tiên là tên > tuổi > điểm.
#
# Nếu đầu vào là:
#
# Tom, 19, 80
# John, 20, 90
# Jony, 17, 91
# Jony, 17, 93
# Json, 21, 85
#
# Thì đầu ra sẽ là:
#
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# from operator import itemgetter, attrgetter
# lis = []
# while True:
#     s = input("input: ")
#     if not s:
#         break
#     lis.append(tuple(s.split(",")))
# print(sorted(lis, key=itemgetter(0,1,2)))

##################################################################################################
# bài 24
# import math
# res = [0,0]
# while True:
#     s = input("input: ")
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = movement[1]
#     if direction == "U":
#         res[0]+=int(steps)
#     elif direction == 'D':
#         res[0]-=int(steps)
#     elif direction == 'L':
#         res[1]-=int(steps)
#     elif direction == 'R':
#         res[1]+=int(steps)
#     else:
#         pass
# print(int(round(math.sqrt(res[0]**2+res[1]**2))))

##################################################################################################
# bài 25:
# Câu hỏi:
# Viết chương trình tính tần suất các từ từ input. Output được xuất ra khi sắp xếp theo bảng chữ cái
# Giả sử input: New to Python or choosing between Python 2 and Python3? Read Python 2 and Python 3.
# thì out put là:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:

# res = {}
# line = input()
# for word in line.split():
#     res[word] = res.get(word,0)+1
# words = sorted(res.keys())
# for w in words:
#     print("%s:%d" %(w, res[w]))