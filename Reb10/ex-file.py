"""
Name : wanwisa juanan
ID : 364411760002
Group : MIT421
"""

# File I/0

# open file

f = open("test.txt")
print(f.read())   # read all text in a file
f.close()

f = open("test.txt")
print(f.read(10)) # read 10 charecters from file
f.close()

f = open("test.txt")
print(f.readline())
print(f.readline())
f.close()


f = open("text.txt")
line = f.readline() # read line
for x in line:
    print(x)
f.close()

print(line)

count = 1
for x in range(len(line))
    print(count,line[X])
    count ==3:
        break
    count += 1