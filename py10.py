#nested condition in python!!
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
symbol = input("Enter a symbol: ")

for i in range(row):
    for j in range(column):
        print(symbol,end="")
    print() 
