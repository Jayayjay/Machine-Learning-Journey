'''binary search algorithm function takes a sorted array and an item. if the item is in the array, the function returns its position'''

def binary_search(list, item):
    low = 0 
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list [mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else: 
            low = mid + 1 
    return None

my_list = [1,3,5,7,9,11,13,15,27]


print(binary_search(my_list, 1))
print(binary_search(my_list, -1))

