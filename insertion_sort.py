array = [8,7,1,4,9,8,5,3,2,1]

def insertion_sort(array):
    a=array[:]
    comparisons = 0
    for j in range (1, len(a)):
        key = a[j]
        i= j-1

        while i >= 0:
            comparisons+=1
            if a[i] > key:
                a[i+1] = a[i]
                i -=1
            else:
                break
        a[i+1] = key
    return a, comparisons

print(insertion_sort(array))
