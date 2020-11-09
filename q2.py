class MyString:

    def __init__(word, myString):
        word.__myString = myString

    def count(word):
        counting = len(word.__myString.split())
        return counting

    def findMostFrequentChar(word):
        counter = {}
        new_string = list(filter(lambda x: 'a' >= x <= 'z', word.__myString.lower()))
        for char in new_string:

            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        key, value = max(counter.items(), key=lambda x:x[1])
        return value, key


def main():
    aString = MyString("an apple is not a tomato")

    count, letter = aString.findMostFrequentChar()
    print("The most frequent character is",'"', letter,'"', "which appeared", count, "times")

main()
