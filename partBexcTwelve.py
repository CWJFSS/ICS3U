"""Use othello.txt for counting the total number of characters in the file
Use illiad.txt for counting the number of capital letters in the file
Use romeoAndJuliet.txt for counting the number of vowels in the file
Use theOdyssey.txt for counting the number of words in the file
Use hamlet.txt for counting the number of punctuation marks in the file
Use macbeth.txt for finding out the most used letter in the file"""
import os
import collections
"""with open("hamlet.txt",'r') as f:
    p=f.read()

    words=p.split()
    wordCount=len(words)
    charCount=len(p)"""

with open("hamlet",'r') as f:
    message=str(f.read())

    words=message.split()
    wordCount=len(words)
    charCount=len(message)
    
print(wordCount)
print(charCount)

messageHigh=sum(1 for c in message if c.isupper())
print("the amount of capitals is: "+str(messageHigh))
count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))

punct = count(message, string.punctuation)
#print((punct))

count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
print("the most common charcter ____occurs____times "+str(collections.Counter(message).most_common(1)[0]))
print("the vowels aeiou respectively are:")

print(*map(message.lower().count, "aeiou"))
#c:\\user\\%USER%\\Desktop\\folder\\output.txt
#open(r'C:\hamlet.txt')
#THIS_FOLDER = os.path.dirname(os.path.abspath(hamlet.txt))
#my_file = os.path.join(THIS_FOLDER, 'hamlet.txt')
"""
with open('input.txt', 'r') as f:
    p = f.read() # p contains contents of entire file
    # logic to compute word counts follows here...

    words = p.split()

    wordCount = len(words)
    print "The total word count is:", wordCount

    # you want the top N words, so grab it as input
    N = int(raw_input("How many words do you want?"))

    c = Counter(words)
    for w, count in c.most_common(N):
       print w, count"""
