"""
Name : wanwisa juanan
ID : 364411760002
Group : MIT421
"""

#  Excepion
print("Start")

while True:
    try:
        num = int(input("Enter an integer: "))
        print(f'Your number is {num}')
        break
    except ValueError as e:
        print("Error log: ",e.args)
        print("Please, enter only integer.")


print("End")