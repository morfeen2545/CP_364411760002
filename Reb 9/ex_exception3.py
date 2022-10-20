"""
Name : wanwisa juanan
ID : 364411760002
Group : MIT421
"""

def division(a,b):
    try:
        return a/b
    except:
        raise  ZeroDivisionError("divide by zero")

try:
    rs = division(10,0)
    print("The resulf: ",rs)
except Exception as e:
    print("Error log: ",e.args)


print("End")