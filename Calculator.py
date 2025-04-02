print("Please select an option")
print("a. Add \nb. Subtract \nc. Multiply \nd. Divide")
choice=input("Enter a choice: ")
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

if choice=='a':
    print(num1,'+',num2,'=',add(num1,num2))
elif choice=='b':
    print(num1,'-',num2,'=',subtract(num1,num2))
elif choice=='c':
    print(num1,'x',num2,'=',multiply(num1,num2))
elif choice=='d':
    print(num1,'/',num2,'=',divide(num1,num2))
else:
    print("Invaild options. Enter again")