x=int(input("How Many Times you want to run?"))
i=1
total=0
while(i<=x):
    expense=int(input("Enter Montly Expense"))
    total=total+expense
    i=i+1

print("Total Expense:",total)