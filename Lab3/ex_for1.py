"""
Name : wanwisa juanan
ID : 364411760002
Group : MIT421
"""

# for loop

# range

for x in range(10):
    print(x,end="-")


# 1-10
for x in range(1,11):
    print(x,end="-")
#เเสดงตัวเลขตั้งเเต่ 1-100 ที่หารด้วย 5 ลงตัว
for x in range(5,101,5):
    print(x,end="-")

# เเสดงตัวเลขตั้งเเต่ 1-100 ที่หารด้วย 3 เเละ 5 ลงตัว
print("")
for x in range(1,101,):
    if x%3==0 and x%5==0:
        print(x,end="-")

