import sys

argv = sys.argv
argvLen = len(argv)
if argvLen < 2:
    print("No file name provided")
    exit(1)

fileName = argv[1]
print("Parsing file " + fileName)

file = open(fileName, "r")

words = []
lineNumber = 0
while True:
    line = file.readline()
    if not line:
        break

    lineNumber += 1
    line = line.replace("\n", "")
    lineWords = line.split(" ")
    for word in lineWords:
        wordUpper = word.upper()
        if wordUpper in words:
            print("Found duplicate word '{}' on line {}".format(word, lineNumber))
        else:
            words.append(wordUpper)
