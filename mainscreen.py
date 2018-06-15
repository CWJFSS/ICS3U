#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel
#uses hash function with 3 users to show assignments A and B
#ASSINGMENT 2 First encryption method
#import relevant libraries
import uuid
import hashlib

#open text file, specify read, set variable as f
with open('database.txt', 'r') as f:
    content= f.readlines()
    #print(content[0])
    print (content)
    #strip the newline
    lines = [line.rstrip('\n') for line in content]
    print (lines)


    #predefined function
    codify = uuid.uuid4().hex
#USES A HASH FUNCTION: ONLY ENCRYPTS USING SHA WITH 24 BIT KEY. CONVERTS IT TO HEXIDECIMAL FOR ALL THE LINES IN THE PASSWORD DATABASE TEXT FILE
    hashedA=(hashlib.sha224(codify.encode() + lines[0].encode()).hexdigest() + ':' + codify)
    hashedB=(hashlib.sha224(codify.encode() + lines[1].encode()).hexdigest() + ':' + codify)
    hashedAB=(hashlib.sha224(codify.encode() + lines[2].encode()).hexdigest() + ':' + codify)

    input_pass=(hashlib.sha224(codify.encode() + input('Please enter a password: ').encode()).hexdigest() + ':' + codify)
    #gets input
    #checks if hashed function is equal to the user input hashed function
    if input_pass==hashedA:
	#get assignmentA
        import house
		import arcs
		import partAnum3
		import exc4partA
		import exc5partA
		import circlefollowmouse
		import assignmentApartLast
		
    if input_pass==hashedB:
	#assignment B
		import partBexcNine
		import partBexcTen
		import partBexcEleven
		import partBexcTwelve
		
    if input_pass==hashedAB:
	#gets everything
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
#end
    





    
