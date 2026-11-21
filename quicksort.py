def quicksort(array):
    length = len(array)
    if length <=1:
        return array
    else:
        pivot=array.pop()

        items_greater=[]
        items_lower=[]

        for item in array:
            if item >pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return quicksort(items_lower) + [pivot] + quicksort(items_greater)


array = [8,7,1,4,9,8,5,3,2,1]
print(quicksort(array))