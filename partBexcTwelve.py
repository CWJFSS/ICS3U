"""Use othello.txt for counting the total number of characters in the file
Use illiad.txt for counting the number of capital letters in the file
Use romeoAndJuliet.txt for counting the number of vowels in the file
Use theOdyssey.txt for counting the number of words in the file
Use hamlet.txt for counting the number of punctuation marks in the file
Use macbeth.txt for finding out the most used letter in the file"""
import os
import collections


with open("illiad.txt",'r') as a:
    message1=str(a.read())    
with open("othello.txt",'r') as b:
    message2=str(b.read())
    
with open("romeoAndJuliet.txt",'r') as c:
    message3=str(c.read())
    
with open("theOdyssey.txt",'r') as d:
    message4=str(d.read())

with open("macbeth.txt",'r') as e:
    message5=str(e.read())

with open("hamlet.txt",'r') as f:
    message=str(f.read())
    
words=message4.split()
wordCount=len(words)
charCount=len(message2)
    
print(wordCount)
print(charCount)

messageHigh=sum(1 for c in message1 if c.isupper())
print("the amount of capitals is: "+str(messageHigh))
count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))

punct = count(message, string.punctuation)


count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
print("the most common charcter ____occurs____times "+str(collections.Counter(message5).most_common(1)[0]))
print("the vowels aeiou respectively are:")

print(*map(message3.lower().count, "aeiou"))
