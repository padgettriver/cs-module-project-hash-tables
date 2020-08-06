def no_dups(s):
    newString = s.split()
    myDict = {}

    for x in newString:
        myDict[x] = 1

    preAnswer = list(myDict.keys())
    answer = ""

    for x in preAnswer:
        answer += str(x) + " "

    answer = answer[:-1]

    return answer



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))