
  
# This function does the sorting of the numbers contained
# in the array in the range defined by the start and 
# end points
def partition(start, end, array):
      
    # Pivot's index is initialized as the start point
    pivot_index = start 
    pivot = array[pivot_index]

    # The following loop will run until the start
    # index crosses the end index. When that happens,
    # it means that the correct ordered position for the pivot
    # in the array was found and it its the end index position,
    # so we swap it.
    while start < end:
        
        # Increments the start index until it finds and element
        # greater than the pivot.
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrements the end index until it finds an
        # element less than the pivot
        while array[end] > pivot:
            end -= 1

        # If the start and end point have not crossed each other
        # the numbers on both indexes are swapped and 
        # the process continues
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.

    # When this part is reached, it means the start and end point have crossed
    # each other and the correct position for the pivot was found, so
    # we swap the element at the pivot index with the element at the end index.
    # We know it is the right position because now we know that every element 
    # to the left of the pivot is less than it, and every element
    # to the right is greater than it.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returns the end index so the array is divided into two parts
    # and the sorting is done separately
    return end
      
def sort(start, end, array):
      
    if (start < end):
          
        partition_index = partition(start, end, array)
          
        # Sort elements before partition 
        # and after partition
        sort(start, partition_index - 1, array)
        sort(partition_index + 1, end, array)
        

def run(array):
    sort(0, len(array) - 1, array)
    return array

