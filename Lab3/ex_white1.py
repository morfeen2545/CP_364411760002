"""
Name : wanwisa juanan
ID : 364411760002
Group : MIT421
"""

# while loop

# รับค่าจากผู้ใช้ไปเรื่อยๆ เเต่หากใช้ใส่ค่าเลข 0 ให้หยุดการทำงานของลูป22
i = 0
while i < 10:
    num = int(input("Enter an integer: "))
    print("your number is : ",num)
    if num ==0:
        print("good bye.")
        continue # continue
    i += 1

