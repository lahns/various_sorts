def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        L = x[:mid]
        R = x[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                x[k] = L[i]
                i=i+1
            else:
                x[k] = R[j]
                j = j + 1
            k = k + 1

        while i < len(L):
            x[k] = L[i]
            i = i+1
            k = k+1
  
        while j < len(R):
            x[k] = R[j]
            j = j+1
            k = k+1

x = [5,4,6,4,3,6,45,436,434,343,5456,46,456,456,34552,454]
print(x)
mergeSort(x)
print(x)