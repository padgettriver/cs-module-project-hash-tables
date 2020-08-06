def word_count(s):
    # Your code here
    origString = s.lower()
    removedChars = '":;,.-+=/\|][}{()*^&'
    newString = origString
    for character in removedChars:
        newString = newString.replace(character, "")
    splitString = newString.split()

    wordCount = {}

    for x in splitString:
        if not wordCount.get(x):
            wordCount[x] = 1
        else:
            wordCount[x] = wordCount[x] + 1



    return wordCount


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))