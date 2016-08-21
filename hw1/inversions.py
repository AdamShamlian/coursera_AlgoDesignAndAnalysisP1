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
    
    target = r"https://d18ky98rnyall9.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1471737600&Signature=APG2s6NbRn-Aew34U2qk8ScR84si8W8AG7UAuBwMm2dM1TaDKjJUyUY4foETthUc1vra8YqFZrjcAqo2e4xzFbZBQeYUkSPkLSnUnYlTlFpEp54tcMahM~lbpKDZF7SJhpOCLChul2lOUr9olCPLOqXVMlNyYyGZjp3cAST07Kc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    data = urllib2.urlopen(target)

    inputArray = []
    for line in data:
        inputArray.append(line)

    print(get_num_inversions(inputArray))