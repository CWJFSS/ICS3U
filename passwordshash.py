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

    hashedA=(hashlib.sha256(codify.encode() + lines[0].encode()).hexdigest() + ':' + codify)
    hashedB=(hashlib.sha256(codify.encode() + lines[1].encode()).hexdigest() + ':' + codify)
    hashedAB=(hashlib.sha256(codify.encode() + lines[2].encode()).hexdigest() + ':' + codify)

    input_pass=(hashlib.sha256(codify.encode() + input('Please enter a password: ').encode()).hexdigest() + ':' + codify)
    
    
    if input_pass==hashedA:
        print("good")
    if input_pass==hashedB:
        print("leboi")
    if input_pass==hashedAB:
        print("dasmaboi")
    else:
        print("bad")

        
    """new_pass = input('Please enter a password: ')
    if new_pass==lines[0]:
        print("good")
    else:
        print("bad")"""



"""def hash_password(password):
    # uuid is used to generate a random number
    codify = uuid.uuid4().hex
    return hashlib.sha256(codify.encode() + password.encode()).hexdigest() + ':' + codify

def check_password(hashed_password, user_password):
    password, codify = hashed_password.split(':')
    return password == hashlib.sha256(codify.encode() + user_password.encode()).hexdigest()"""
"""def hash_password(password):
    # uuid is used to generate a random number
    codify = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + codify
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
#if check_password(hashed_password, old_pass):
#    import house
#    import arcs
#    import partAnum3
#    import exc4partA
#    import exc5partA
#    import circlefollowmouse
#    import assignmentApartLast
    
if check_password(hashed_password, old_pass):
    #import partBexcNine
    #import partBexcTen
    #import partBexcEleven
    #import partBexcTwelve

if check_password(hashed_password, old_pass):
import all




    
else:
    print('I am sorry but the password does not match')"""
