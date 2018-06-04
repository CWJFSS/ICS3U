#Made by: CW
#date: 5/27/17
#teacher: Mr. Seidel
#uses hash function with 3 users to show assignments A and B


import uuid
import hashlib


with open('database.txt', 'r') as f:
    content= f.readlines()
    #print(content[0])
    print (content)
    #newstr = content[0].replace("/n", "")
    lines = [line.rstrip('\n') for line in content]
    print (lines)


    
    codify = uuid.uuid4().hex

    hashedA=(hashlib.sha224(codify.encode() + lines[0].encode()).hexdigest() + ':' + codify)
    hashedB=(hashlib.sha224(codify.encode() + lines[1].encode()).hexdigest() + ':' + codify)
    hashedAB=(hashlib.sha224(codify.encode() + lines[2].encode()).hexdigest() + ':' + codify)

    input_pass=(hashlib.sha224(codify.encode() + input('Please enter a password: ').encode()).hexdigest() + ':' + codify)
    
    
    if input_pass==hashedA:
	
        import house
		import arcs
		import partAnum3
		import exc4partA
		import exc5partA
		import circlefollowmouse
		import assignmentApartLast
		
    if input_pass==hashedB:
	
		import partBexcNine
		import partBexcTen
		import partBexcEleven
		import partBexcTwelve
		
    if input_pass==hashedAB:
        import house
		import arcs
		import partAnum3
		import exc4partA
		import exc5partA
		import circlefollowmouse
		import assignmentApartLast
		import partBexcNine
		import partBexcTen
		import partBexcEleven
		import partBexcTwelve
    else:
        print("Your password does not exist. Please try again ")

    





    
