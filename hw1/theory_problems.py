class SecondLargestElementFinder(object):
    
    """ An implementation of the algorithm to Optional Theory Problems 1-1 for 
    Coursera's Stanford's Design and Analysis of Algorithms, Part 1. 

    This is implemented as a class primarily to make the function signatures cleaner.
    By storing 'eliminated' elements in an instance variable, we don't need to pass 
    clunky data structures between functions and recursive calls. """

    def __init__(self, array):
        super(SecondLargestElement, self).__init__()
        self.array = array

        assert np.log(len(self.array)) % 1 == 0, 'The array length must be a power of two.'
        assert len(a) == len(set(a)), 'The array must contain distinct integers.'

        self._storage = {str(x): [] for x in self.array} # I prefer strings over numerals as dict keys


    def _find_max_by_twos(self, a):
        """ Embedded in _prep_second_largest, this runs in n-1 time. """
        
        tmp = []

        for i in range(0, len(a), 2):

            if a[i] > a[i+1]:
                self._storage[str(a[i])].append(a[i+1])
                binMax = a[i]

            else:
                self._storage[str(a[i+1])].append(a[i])
                binMax = a[i+1]

            tmp.append(binMax)

        return tmp


    def _prep_second_largest(self, a):
        """ The divide and conquer of the broader algorithm. The operations in this function are 
        constant, but the embedded function runs in n-1 time. """
        
        if len(a) == 2:

            if a[0] > a[1]:
                self._storage[str(a[0])].append[a[1]]
                arrayMax = str(a[0])

            else:
                self._storage[str(a[1])].append(a[0])
                arrayMax = str(a[1])

            return arrayMax # returned as a string to match dict key

        return _prep_second_largest(_find_max_by_twos(a))


    def find_second_largest(self, a):
        """ Used to more legibly find the second largest element in the provided array. 
        This runs in log(n) - 1 time. """
        
        self.__init__(a) # this guarantees you could run this again
        arrayMax = self._prep_second_largest(a) # this is the meat and potatoes

        arraySecondMax = 0

        for i in range(len(self._storage[arrayMax])):

            if a[i] > arraySecondMax:
                arraySecondMax = a[i]

        return arraySecondMax





def find_unimodal_max(inputArray):
    """ Determine the maximal element in a unimodal array. This runs in O(log n) time,
    as it's essentially a binary search."""
    
    halfIdx = int(len(inputArray) / 2 + 0.5) # guarantees we optimally split the array (integer truncation)

    if len(inputArray) == 2: # more explicit than the "quicker" check that halfIdx == 1
        return inputArray[1] if inputArray[1] > inputArray[0] else inputArray[0]

    # recall, n DISTINCT elements, so only need to worry about < or >
    if inputArray[halfIdx-1] < inputArray[halfIdx]: 
        # max must be in array[halfIdx:] because of the montone nature in the two subarrays, a_inc and b_dec
        return unimodal_max(inputArray[halfIdx:])
    
    else:
        # same but in opposite direction
        return unimodal_max(inputArray[:halfIdx])



def check_linearly_index_equals_element(inputAarray):
    """ Here's the O(n) case, which is more or less trivial. Can we do better? 
    Let's try to take advantage of the sortedness of the array. """
    
    arrayLength = len(inputAarray)

    for i in range(arrayLength):

        if inputAarray[i] == i or inputAarray[-i] == -i:
            return True
    return False 



def check_sublinearly_index_equals_element(inputAarray, i):
    """ While technically O(n) in the worst case, this should perform better than
    the naive search. 

    NOTE: This is SIMILAR to http://stackoverflow.com/questions/4172580/interview-question-search-in-sorted-array-x-for-index-i-such-that-xi-i
    provided solution. 

    NOTE: Also, my interpretation of using negative indices may make this impossible 
    to execute in truly O(log n). In the case of purely positive index calls, this is the same
    solution. """
    
    if inputAarray[i] == i or inputAarray[-i] == -i:
        return True
    if i == -1 or i >= len(inputAarray)-1: 
        return False

    if inputAarray[i] >= 0:
        return take_two(inputAarray, inputAarray[i] - i)
    else:
        return take_two(inputArray, inputAarray[i] - len(inputAarray))