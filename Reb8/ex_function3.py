"""
Name : wanwisa juanan
ID : 364411760002
Group : MIT421
"""

# function with keyword parameter

def myfunc(msg = "MIT"):
    print("Hello,",msg)

# calling function with default parameter
myfunc()
myfunc("Thungsong")

# function with keyword parameter
def myfunc2(num1,num2,num3):
    print(num1,num2,num3)
# calling function with keyword parameter
myfunc2(num3=30,num1=10,num2=20)

# function with multiple keyword parameter
def myfunc3(**data): # **value --> dictionary
    print(data)
    print(data.keys())
    print(data.values())

# key=value
myfunc3(name="sam",major="MIT")
