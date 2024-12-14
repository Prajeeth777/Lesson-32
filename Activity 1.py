name="Ali"
age=5
weight=20.8
isStudent=True

print("Data type of ",name," before type casting is ",type(name))
print("Data type of ",age," before type casting is ",type(age))
print("Data type of ",weight," before type casting is ",type(weight))
print("Data type of ",isStudent," before type casting is ",type(isStudent))

age=str(age)
weight=int(weight)
isStudent=str(isStudent)

print("Data type of ",age," before type casting is ",type(age))
print("Data type of ",weight," before type casting is ",type(weight))
print("Data type of ",isStudent," before type casting is ",type(isStudent))