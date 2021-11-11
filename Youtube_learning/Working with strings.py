# Working with strings
#print("Giraffe \n Academy")        # put (\n) for next line
#print("GIraffe \" Academy")        # put (\") to rpint the quotation ark

phrase = "Giraffe Academy"
#print(phrase  + "is cool")                      #concatenation
print(phrase.lower())                            #lower is a function that converts every in lowercase
print(phrase.upper())

print(len(phrase))                               # length of the string
print(phrase[5])                                 # INdexing. It starts with 0. i.e G is 0
print(phrase.index("Acad"))                         #  passing a parameter

print(phrase.replace("Giraffe","Mandaar"))