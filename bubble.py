
x = [5,4,6,4,3,6,45,436,434,343,5456,46,456,456,34552,454]
print(x)
for i in range(len(x)):
    for j in range(len(x)):
        if(x[i]<x[j]):
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
print(x)