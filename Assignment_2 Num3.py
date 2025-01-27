from math import sqrt
D = input("Enter a sequence of number to find square root of them: ")
list1 = D.split(',')
C = 50
H = 30
list2 = []
for num in list1:
    Operation = (2 * C * int(num)) / H
    Q = round(sqrt(Operation))
    list2.append(Q)
string = str(list2).replace('[', '').replace(']', '')
print(string)

