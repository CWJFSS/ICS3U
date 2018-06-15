#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel

#get libraries
import string
import collections
"""The length (in characters) of the sentence (e.g. 60 characters)
The number of capital letters in the sentence (e.g. 1)
The number of vowels in the sentence (always exclude 'y') (e.g. 20)
The number of words in the sentence (e.g. 10)
The number of punctuation marks in the sentence (count ', :, ;, ., ,, !, ? only) (e.g. 2)
The most used letter in the sentence (e.g. e : 6)


"""

#use variables to define what you want
message = "Whatever you put here, it must always be school appropriate."
co = lambda val1, val2: len(list(filter(lambda a: a in val2, val1)))

#punctuation
punct = co(message, string.punctuation)
#mostUsed


print("the most common charcter ____occurs____times "+str(collections.Counter(message).most_common(1)[0]))

length=len(message)
#vowels
words= int(message.co(' '))


messageHigh=sum(1 for a in message if a.isupper())
#prints all the necessary items
print("the length is: " +str (length))
print("the amount of words are: "+str(words+1))
print("the vowels aeiou respectively are:")
print(*map(message.lower().co, "aeiou"))
print("the amount of words are: "+str((punct)))

print("the amount of capitals is: "+str(messageHigh))


