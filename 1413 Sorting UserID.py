print('Iyai Bassey 1937369') # This is my name and PSID
num_calls = 0
# fucntion for partiton
def partition(IDs, i, k):
    low = (i-1)
    mid = (i+k)//2
    pivot = IDs[mid]
    IDs[mid],IDs[k] = IDs[k],IDs[mid]
    for j in range(i , k):
        if IDs[j] <= pivot:
            low = low+1
            IDs[low],IDs[j] = IDs[j],IDs[low]
    IDs[low+1],IDs[k] = IDs[k],IDs[low+1]
    return (low + 1)

# function for quick sort
def quicksort(IDs, i, k):
    global num_calls
    num_calls+=1
    if i < k:
        pivot_index = partition(IDs, i, k)
        quicksort(IDs, i, pivot_index-1)
        quicksort(IDs, pivot_index+1, k)

# main function as you given
if __name__ == "__main__":
    IDs = []
    ID = input()
    while ID != "-1":
        IDs.append(ID)
        ID = input()
    quicksort(IDs, 0, len(IDs) - 1)
    print("Output is :")
    print(num_calls)
    for ID in IDs:
        print(ID)