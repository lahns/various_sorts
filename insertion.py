def insertion(A,n):
    if n > 0:
        insertion(A, n-1)
        x = A[n]
        j = n-1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x


x = [5,4,6,4,3,6,45,436,434,343,5456,46,456,456,34552,454]
print(x)
insertion(x,len(x)-1)
print(x)