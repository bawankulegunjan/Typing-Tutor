#L = list(input("Enter the elements of list :\n"))
n1 = int(input("Total Pages :"))
L1 = [2,4,5,8,12,13,16,23]
print(L1)

min = 1
max = n1 
L = []
for i in range(min, max + 1):
    if i in L1:
        continue
    else:
        L.append(i)
print("Missing pages:\n")
print(sorted(L))
