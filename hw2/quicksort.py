""" Unfortunately, I cannot get this to provide the correct answer. It 
is highly likely that I have misinterpreted the partition algorithm (which
appears in first_element_pivot()). Fortunately, I have tested the sorted
output against python, and I have found that the resulting array is indeed
sorted. """


def load_array(location):
    """ DocString"""
    
    toBeSorted = []

    with open(location) as f:

        for line in f.readlines():
            toBeSorted.append(int(line))

    return toBeSorted



def quicksort(inputArray, method='first'):
    """ QUICKSORT! The idea of this algorithm can be somewhat trivialized with list comprehensions, but w/e. """
    

    if len(inputArray) <= 1: # we can get an empty array if the pivot is the smallest or largest element in the array
        return inputArray

    else:
    
        global comparisonCount 
        comparisonCount += len(inputArray) - 1

        if method == 'first':
            inputArray, j = first_element_pivot(inputArray)

        elif method == 'last':
            inputArray, j = last_element_pivot(inputArray)

        elif method == 'median':
            inputArray, j = median_element_pivot(inputArray)

        else:
            raise NotImplementedError("Try 'first', 'last', or 'median'.")

    return quicksort(inputArray[1:j]) + [inputArray[0]] + quicksort(inputArray[j:]) # < pivot, pivot, > pivot


def first_element_pivot(inputArray):
    """ The pivot subroutine given that we must take the first element of the array as pivot. """

    pivot = inputArray[0]
    j = 1

    for i in range(1, len(inputArray)):

        if inputArray[i] < pivot:

            inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
            j+=1 # increment the spot to switch to

    return inputArray, j


def last_element_pivot(inputArray):
    """ Pivot subroutine given that we must take the last element of the array as pivot.
    As specified by the problem, switch the first and last elemetn and proceed. """
    
    inputArray[0], inputArray[-1] = inputArray[-1], inputArray[0]
    return first_element_pivot(inputArray)


def median_element_pivot(inputArray):
    """ Pivot subroutine given that we must use a 'median' element of the array as pivot. """

    midIdx = len(inputArray) // 2 + len(inputArray) % 2

    # there are only 3 options here...
    if inputArray[0] <= inputArray[midIdx] <= inputArray[-1] or inputArray[-1] <= inputArray[midIdx] <= inputArray[0]:
        inputArray[0], inputArray[midIdx] = inputArray[midIdx], inputArray[0]

    elif inputArray[0] <= inputArray[-1] <= inputArray[midIdx] or inputArray[midIdx] <= inputArray[-1] <= inputArray[0]:
        inputArray[0], inputArray[-1] = inputArray[-1], inputArray[0]

    else:
        pass # already in proper form

    return first_element_pivot(inputArray)


# using a global variable to be incremented is easier, but is more error prone and requires manual resets 
# after each use 
comparisonCount = 0


def count_comparisons(inputArray, method='first'):
    """ Wraps the counting of comparisons so we don't have to manually reset the counter variable. """
    
    global comparisonCount
    comparisonCount = 0

    sortedArray = quicksort(inputArray, method)

    print('The number of {0} comparisons is: {1}'.format(method, comparisonCount))
    return sortedArray, comparisonCount


def main():
    """ Call load_array each time for fresh array """
    
    location = r"a;ldfjals;dj"

    loaded = load_array(location)
    count_comparisons(loaded, 'first')

    loaded = load_array(location)
    count_comparisons(loaded, 'last')

    loaded = load_array(location)
    count_comparisons(loaded, 'median')

    return 


if __name__ == '__main__':
    
    main()