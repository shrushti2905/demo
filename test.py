role=input("enter your role: ")
age=int(input("enter your age: "))

print(f"eligible : ",["false","true"][age<21 and role=="student"])

#hello