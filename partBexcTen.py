import string
import collections
"""The length (in characters) of the sentence (e.g. 60 characters)
The number of capital letters in the sentence (e.g. 1)
The number of vowels in the sentence (always exclude 'y') (e.g. 20)
The number of words in the sentence (e.g. 10)
The number of punctuation marks in the sentence (count ', :, ;, ., ,, !, ? only) (e.g. 2)
The most used letter in the sentence (e.g. e : 6)


"""
message = "Whatever you put here, it must always be school appropriate."
co = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))

#punctuation=
punct = co(message, string.punctuation)
#mostUsed=


print("the most common charcter ____occurs____times "+str(collections.Counter(message).most_common(1)[0]))

length=len(message)
#vowel=*map(message.lower().co, "aeiou")
words= int(message.co(' '))


messageHigh=sum(1 for c in message if c.isupper())
print("the length is: " +str (length))
print("the amount of words are: "+str(words+1))
print("the vowels aeiou respectively are:")
print(*map(message.lower().co, "aeiou"))
print("the amount of words are: "+str((punct)))

print("the amount of capitals is: "+str(messageHigh))


