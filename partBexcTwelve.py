"""Use othello.txt for counting the total number of characters in the file
Use illiad.txt for counting the number of capital letters in the file
Use romeoAndJuliet.txt for counting the number of vowels in the file
Use theOdyssey.txt for counting the number of words in the file
Use hamlet.txt for counting the number of punctuation marks in the file
Use macbeth.txt for finding out the most used letter in the file"""

#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel
#get libraries
import os
import collections

#read all the files and set as variables
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
#counts words    
words=message4.split()
wordCount=len(words)
#counts characters
charCount=len(message2)
#prints it    
print(wordCount)
print(charCount)
#gets capitals
messageHigh=sum(1 for c in message1 if c.isupper())
print("the amount of capitals is: "+str(messageHigh))

amt = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
#gets all the punctuations
punct = amt(message, string.punctuation)


amt = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
#gets most common
print("the most common charcter ____occurs____times "+str(collections.Counter(message5).most_common(1)[0]))
print("the vowels aeiou respectively are:")
#gets all the vowels
print(*map(message3.lower().amt, "aeiou"))
