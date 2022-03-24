from re import L

# Function reads the file with all possible wordle answers.
def readFile():
    wordString = ""
    words = []
    stripedWords = []

    with open("answer.txt") as f:
        for line in f:
            wordString += line.strip()

    words = wordString.split(',')

    for word in words:
        stripedWords.append(word.strip())

    return stripedWords

def playWordle(wordList):
    while (len(wordList) > 1):
        inputWord = input("What five letter word did you try? ").lower()
        print("For each letter in the wordle board type a corresponding key:")
        print("For example (X = Not in Word, Y = In word WRONG position, G = In word RIGHT position")
        letterKey = input("Input which letters were correct based on key above: ").lower()

        wordsToRemove = []
        wordLetters = []

        for i in range(len(inputWord)):
            for words in wordList:
                if letterKey[i] == 'x':
                    if inputWord[i] in words:
                        if inputWord[i] not in wordLetters:
                            wordLetters.append(inputWord[i])
                        elif words[i] == inputWord[i]:
                            wordsToRemove.append(words)
                elif letterKey[i] == 'y':
                    if inputWord[i] not in words:
                        wordsToRemove.append(words)
                    elif words[i] == inputWord[i]:
                        wordsToRemove.append(words)
                    if inputWord[i] not in wordLetters:
                            wordLetters.append(words)
                elif letterKey[i] == 'g':
                    if words[i] != inputWord[i]:
                        wordsToRemove.append(words)
                    if inputWord[i] not in wordLetters:
                            wordLetters.append(words)

                    
        guess = input("Was your guess correct? (Y or N)").lower()
        if guess == 'y':
            print("Congratulations on keeping that streak")
            return
        elif inputWord in wordList:
            wordsToRemove.append(inputWord)
        
        for words in wordsToRemove:
                if words in wordList:
                    wordList.remove(words)
        
        for word in wordList:
            print(word)
        

def main():
    wordList = readFile()
    playWordle(wordList)

main()