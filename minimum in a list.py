# Finding the minimum number in a list

list_1 = []
list_2 = []
min = None

X = int(input("How many numbers will you enter? "))

while True:
    x = int(input("Enter the numbers: "))
    list_1.append(x)
    if len(list_1) == X:
        break

for el in list_1:
    if min is None:
        min = el
    if el < min :
        min = el
print(min)