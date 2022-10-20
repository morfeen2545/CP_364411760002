"""
Name : wanwisa juanan
ID : 364411760002
Group : MIT421
"""

# create file
import os
# create empty file
try:
    f = open("test2.txt","x")
    f.close()
except:
    print("File already exits.")

# create test3.txt on desktop of your computer
#C:\Users\LabCom_MT-4\Desktop
try:
    f = open("C:\\Users\LabCom_MT-4\\test3.txt","x")
    f.close()
except Exception as e:
    print(e)


# write file
# mode "a" ,"w"
try:
    f = open("test2.txt","w")
    f.write("Wanwisa Juanan\n")
except:
    print("Cloud not found a fine name 'test2.txt")
finally:
    f.close()

# delete file

if os.path.exists("test3.txt"):
    os.remove("test2.txt")
else:
    print("File not found.")