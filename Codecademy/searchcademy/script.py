#In order to test a product, many companies use empty or “fake” data. Our company, Searchcademy, uses empty sparsely sorted data to test its awesome search engine. What exactly does that mean? Sparsely Sorted Data is data such that there is empty data in between the sorted values.

#In this project, we will implement a modified version of iterative binary search to search through a sparsely sorted dataset.

def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))
    
    first = 0
    last = len(data) -1

    while first <= last:

        mid = (first + last) // 2

        #since sparse data set, need to check if middle is empty
        if data[mid] == "":
            left = mid - 1
            right = mid + 1

            #searching for the next position with a value
            while(True):
                if (left < first) or (right > last):
                    print('{0} is not in the dataset'.format(search_val))
                    return

                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break
                else:
                    right += 1
                    left -= 1

        #returns out if the mid value equals the search value
        if data[mid] == search_val:
            print('{0} found at position {1}'.format(search_val, mid))
            return
            
        #if search value is less than mid, searches left half of list
        if search_val < data[mid]:
            last = mid - 1

        #if search value is greater than mid, searches right half of list
        if search_val > data[mid]:
            first = mid + 1

    print('{0} is not in the dataset'.format(search_val))