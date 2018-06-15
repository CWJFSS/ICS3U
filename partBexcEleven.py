#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel
import string
import collections
"""The length (in characters) of the sentence (e.g. 60 characters)
The number of capital letters in the sentence (e.g. 1)
The number of vowels in the sentence (always exclude 'y') (e.g. 20)
The number of words in the sentence (e.g. 10)
The number of punctuation marks in the sentence (count ', :, ;, ., ,, !, ? only) (e.g. 2)
The most used letter in the sentence (e.g. e : 6)



VOWELS = "aeiou"
vowels_count = len([char for char in sentence if char in VOWELS])
"""
message = "Whatever you put here, it must always be school appropriate."
amt = lambda val1, val2: len(list(filter(lambda a: a in val2, val1)))

#punctuation=
#mostUsed=

def mostcommon():
    return(collections.Counter(message).most_common(1)[0])
print(mostcommon())


def length():
    return (len(message))
print(length())

#vowel=*map(message.lower().amt, "aeiou")




def vo():
    numVo=0
    for char in message:
        if char in "aeiou":
           numVo = numVo+1
    return numVo
print(vo())


def punctu():
    return(amt(message, string.punctuation))

print(punctu())


def messageHigh():

    return(sum(1 for a in message if a.isupper()))
    
print(messageHigh())


def words():
    return message.amt(' ')+1

print(words())

