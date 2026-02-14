#splitting list into even and odd no's
lst = [1, 2, 3, 4, 5, 6,7]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even list:", even)
print("Odd list:", odd)
