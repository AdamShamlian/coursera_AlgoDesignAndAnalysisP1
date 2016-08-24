import urllib2


def get_num_inversions(inputArray):
    """ Wrapper function for some convenience. """
    return sort_and_count_inversions(inputArray, len(inputArray))[1] # count only


def sort_and_count_inversions(inputArray, length):
    """ This comes more or less straight from the lectures. """
    
    if len(inputArray) == 1:
        return inputArray, 0

    halfIdx = int(len(inputArray) / 2 + 0.5)
    sortedFirstHalf, countFirstHalf = sort_and_count_inversions(inputArray[:halfIdx], halfIdx)
    sortedSecondHalf, countSecondHalf = sort_and_count_inversions(inputArray[halfIdx:], len(inputArray)-halfIdx)
    sortedArray, countArray = sort_and_count_split_inversions(sortedFirstHalf, sortedSecondHalf)
    return sortedArray, countFirstHalf + countSecondHalf + countArray


def sort_and_count_split_inversions(firstHalf, secondHalf):
    """ This also comes more or less straight from the lectures. """
    
    iFirst, iSecond = 0, 0
    count = 0
    tmp = []

    for i in range(len(firstHalf) + len(secondHalf)):

        # bounds checking and sort
        if iFirst == len(firstHalf):
            tmp.append(secondHalf[iSecond])
            iSecond += 1

        elif iSecond == len(secondHalf):
            tmp.append(firstHalf[iFirst])
            iFirst += 1

        # the inversion counting and sort
        elif firstHalf[iFirst] < secondHalf[iSecond]:
            tmp.append(firstHalf[iFirst])
            iFirst += 1

        else:
            tmp.append(secondHalf[iSecond])
            iSecond += 1
            count += len(firstHalf) - iFirst

    return tmp, count


if __name__ == '__main__':
    
    # download your text file to some location
    location = r"put your location here"

    with open(location) as f:

        inputArray = []
        for line in f.readlines():
            inputArray.append(line.split('\\')[0]) # remember to escape the \ in '\n'
        
    print(get_num_inversions(inputArray))