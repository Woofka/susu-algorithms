# ----- IMPORT -----
import random
import os


# ----- SETTINGS -----
originalFileName          = "rawSequence.txt"
presortedOriginalFileName = "presortedSequence.txt"
finalFileName             = "sortedSequence.txt"
randomSequenceLenght      = 52000       # N (default: 52000)
tempFilesQuanity          = 9           # P (default: 9)
memoryLimit               = 18          # M (default: 18)
delTempFiles              = True
delPresortedFile          = True  # works only if <delTempFiles> is True
checkForSums              = True


# ----- DEFINITIONS -----
def mergeSort(arr):
    # default merge sort
    if len(arr) <= 1:
        return arr
    middle    = len(arr)//2
    leftHalf  = arr[:middle]
    rightHalf = arr[middle:]
    mergeSort(leftHalf)
    mergeSort(rightHalf)
    i = 0; j = 0; k = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            arr[k] = leftHalf[i]
            i += 1
        else:
            arr[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        arr[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        arr[k] = rightHalf[j]
        j += 1
        k += 1
    return arr


def readNumber(file, lostSymbol=""):
    # reads one number from <file> and will add lost symbol before it, if it needs
    symbol = file.read(1)
    number  = ""
    while symbol != " ":
        number += symbol
        symbol = file.read(1)
    return int(lostSymbol + number)


def randomInputFile(seqLenght, fileName):
    # generates <fileName> file which contained random sequence of <seqLenght> element
    file = open(fileName, "w")
    i = 0
    while i < seqLenght:
        number = random.randint(-100000, 100000)
        file.write("%d " % number)
        i += 1
    file.write(".")
    file.close()


def presortInputFile(elementsQuanity, inputFileName, outputFileName):
    # sorts each <elementsQuanity> element from <inputFileName> using merge sort and writes result to <outputFileName>
    inputFile  = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    array      = []
    sortIsDone = False
    symbol     = inputFile.read(1)

    while not sortIsDone:
        if symbol != ".":                       # if it isn't the end of a file
            number = readNumber(inputFile, symbol)
            symbol = inputFile.read(1)
            if len(array) < elementsQuanity:    # if array isn't full yet
                array.append(number)
            else:                               # if it's full
                mergeSort(array)
                for i in array:
                    outputFile.write("%d " % i)
                array = [number]
        else:                                   # if it's the end of a file
            sortIsDone = True
            mergeSort(array)
            for i in array:
                outputFile.write("%d " % i)

    outputFile.write(".")
    inputFile.close()
    outputFile.close()


def filesRW(index, RW, filesQuanity):
    # returns list of <filesQuanity> files opened for reading or writing.
    # file's name is "file <index> <num>.txt"
    return [open("file %d %d.txt" % (index, i), RW) for i in range(filesQuanity)]


def deleteTempFiles(filesQuanity, presortedFileName, deletePresortedFile=False):
    # deletes all "file <index> <num>.txt" files
    # Also will delete <presortedFileName> if <deletePresortedFile> is True
    for i in range(filesQuanity):
        if os.path.isfile(".\\file 0 %d.txt" % i):
            os.remove(".\\file 0 %d.txt" % i)
        if os.path.isfile(".\\file 1 %d.txt" % i):
            os.remove(".\\file 1 %d.txt" % i)
    if deletePresortedFile:
        if os.path.isfile(".\\%s" % presortedFileName):
            os.remove(".\\%s" % presortedFileName)


def seriesSpreading(filesQuanity, inputFileName):
    # spreads all series of <inputFileName> into "file 0 <num>.txt> files
    inputFile = open(inputFileName, "r")
    tempFiles = filesRW(0, "w", filesQuanity)

    curTempFile = 0
    prevNumber = None
    symbol = inputFile.read(1)
    spreadingIsDone = False
    while not spreadingIsDone:
        if symbol != ".":                                           # spreading isn't done
            number = readNumber(inputFile, symbol)
            symbol = inputFile.read(1)
            if prevNumber is None:                                  # first number
                tempFiles[curTempFile].write("%d " % number)
            else:
                if number >= prevNumber:                            # current series
                    tempFiles[curTempFile].write("%d " % number)
                else:                                               # new series
                    if curTempFile + 1 < filesQuanity:
                        curTempFile += 1
                    else:
                        curTempFile = 0
                    tempFiles[curTempFile].write("%d " % number)
            prevNumber = number
        else:                                                       # spreading is done
            spreadingIsDone = True

    inputFile.close()
    for i in tempFiles:
        i.write(".")
        i.close()


def twoFilesMerge(file1, file2, outputFile):
    # merges two files into one
    # each output series forms from two input series
    prevNumber1 = None
    prevNumber2 = None
    symbol1 = file1.read(1)
    symbol2 = file2.read(1)
    num1IsUsed = True
    num2IsUsed = True
    mergingIsDone = False
    while not mergingIsDone:
        if symbol1 != ".":

            if symbol2 != ".":                                  # both streams
                if num1IsUsed:
                    if prevNumber1 is not None:
                        prevNumber1 = number1
                    number1 = readNumber(file1, symbol1)
                    symbol1 = file1.read(1)
                    num1IsUsed = False
                if num2IsUsed:
                    if prevNumber2 is not None:
                        prevNumber2 = number2
                    number2 = readNumber(file2, symbol2)
                    symbol2 = file2.read(1)
                    num2IsUsed = False
                if prevNumber1 is None or prevNumber2 is None:
                    prevNumber1 = number1
                    prevNumber2 = number2
                if number1 >= prevNumber1:
                    if number2 >= prevNumber2:              # current series
                        if number1 <= number2:
                            outputFile.write("%d " % number1)
                            num1IsUsed = True
                        else:
                            outputFile.write("%d " % number2)
                            num2IsUsed = True
                    else:                                   # only first series
                        outputFile.write("%d " % number1)
                        num1IsUsed = True
                else:
                    if number2 >= prevNumber2:              # only second series
                        outputFile.write("%d " % number2)
                        num2IsUsed = True
                    else:                                   # new 2 series
                        prevNumber1 = number1
                        prevNumber2 = number2

            else:                                               # only fisrt stream
                if num1IsUsed:
                    number1 = readNumber(file1, symbol1)
                    symbol1 = file1.read(1)
                    num1IsUsed = False
                if not num2IsUsed:
                    if number1 <= number2:
                        outputFile.write("%d " % number1)
                        num1IsUsed = True
                    else:
                        outputFile.write("%d " % number2)
                        num2IsUsed = True
                else:
                    outputFile.write("%d " % number1)
                    num1IsUsed = True

        else:

            if symbol2 != ".":                                  # only second stream
                if num2IsUsed:
                    number2 = readNumber(file2, symbol2)
                    symbol2 = file2.read(1)
                    num2IsUsed = False
                if not num1IsUsed:
                    if number1 <= number2:
                        outputFile.write("%d " % number1)
                        num1IsUsed = True
                    else:
                        outputFile.write("%d " % number2)
                        num2IsUsed = True
                else:
                    outputFile.write("%d " % number2)
                    num2IsUsed = True

            else:                                               # merging is done
                if not num1IsUsed:
                    outputFile.write("%d " % number1)
                    num1IsUsed = True
                if not num2IsUsed:
                    outputFile.write("%d " % number2)
                    num2IsUsed = True
                mergingIsDone = True


def isSorted(file):
    # will return True if <file> contains sorted sequence
    symbol = file.read(1)
    result = True
    prevNumber = None
    while symbol != ".":
        number = readNumber(file, symbol)
        symbol = file.read(1)
        if prevNumber is None:
            prevNumber = number
        if number < prevNumber:
            result = False
            break
        prevNumber = number
    return result


def fileCopy(file1, file2):
    # copies sequence from <file1> to <file2>
    symbol = file1.read(1)
    while symbol != ".":
        file2.write(symbol)
        symbol = file1.read(1)
    file2.write(".")


def allFilesMerge(filesQuanity, resultFileName):
    # main merging loop. Keeps spreading and merging until <resultFileName> will not contain sorted sequence
    externalSortIsDone = False
    cycle = 1
    while not externalSortIsDone:
        print("Processing %d cycle..." % cycle)
        i = filesQuanity
        reverse = False
        while i > 0:
            if reverse:
                files0 = filesRW(1, "r", filesQuanity)
                files1 = filesRW(0, "w", filesQuanity)
            else:
                files0 = filesRW(0, "r", filesQuanity)
                files1 = filesRW(1, "w", filesQuanity)
            j = 0; k = 0
            while j < filesQuanity - 1:
                twoFilesMerge(files0[j], files0[j+1], files1[k])
                j += 2
                k += 1
            if filesQuanity % 2 == 1:
                fileCopy(files0[j], files1[k])
            i //= 2
            reverse = not reverse
            for file0 in files0:
                file0.close()
            for file1 in files1:
                file1.write(".")
                file1.close()
        resultFile = open(resultFileName, "w")
        if reverse:
            lastFile = open("file 1 0.txt", "r")
        else:
            lastFile = open("file 0 0.txt", "r")
        fileCopy(lastFile, resultFile)
        resultFile.close()
        lastFile.close()
        resultFile = open(resultFileName, "r")
        externalSortIsDone = isSorted(resultFile)
        resultFile.close()
        if not externalSortIsDone:
            seriesSpreading(filesQuanity, resultFileName)
        cycle += 1


def sumCheck(inputFileName, sortedFileName):
    # calculates sums of sequences from <inputFileName> and <sortedFileName> and prints them
    f1 = open(inputFileName, "r")
    f2 = open(sortedFileName, "r")
    sum1 = 0
    sum2 = 0
    sym1 = f1.read(1)
    sym2 = f2.read(1)
    while sym1 != ".":
        dig1 = readNumber(f1, sym1)
        dig2 = readNumber(f2, sym2)
        sym1 = f1.read(1)
        sym2 = f2.read(1)
        sum1 += dig1
        sum2 += dig2
    f1.close()
    f2.close()
    print("\nOriginal sum: %d\nFinal sum:    %d" % (sum1, sum2))


# ----- MAIN PROGRAM -----
print("Generating random sequence...")
randomInputFile(randomSequenceLenght, originalFileName)
print("Presorting original sequence...")
presortInputFile(memoryLimit, originalFileName, presortedOriginalFileName)
print("Series spreading...")
seriesSpreading(tempFilesQuanity, presortedOriginalFileName)
print("Starting external sort...")
allFilesMerge(tempFilesQuanity, finalFileName)
if delTempFiles:
    deleteTempFiles(tempFilesQuanity, presortedOriginalFileName, delPresortedFile)
print("Done!")
if checkForSums:
    sumCheck(originalFileName, finalFileName)
