def partition(x, s, d): #x = tablica s=poczatek d=koniec
    pivot = x[s]
    l = s + 1 # najmniejszy
    h = d # najwiekszy

    while True:
        while l <= h and x[h] >= pivot:
            h = h - 1

        while l <= h and x[l] <= pivot:
            l = l + 1

        if(l <= h):
            x[l], x[h] = x[h], x[l]
        else:
            break

    x[s], x[h] = x[h], x[s]

    return h

def quick_sort(x, s, d):
    if s >= d:
        return

    p = partition(x, s, d)
    quick_sort(x, s, p-1)
    quick_sort(x, p+1, d)

x = [5,4,6,4,3,6,45,436,434,343,5456,46,456,456,34552,454]
print(x)
quick_sort(x,0,len(x)-1)
print(x)