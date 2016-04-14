#Shravan Kumar Chandrasekaran
#sc3940@columbia.edu
#Exercise 3

######################################
#Importing Libraries
from subprocess import call
from sys import argv
from os.path import exists
#####################################
#username = call(["whoami"])

input_arg1, input_arg2 = argv

prompt = ">"

print "Do you like chocolates  %s?" %input_arg2

choc = raw_input(prompt)

print choc, input_arg2

#text = open("ex2.py")

#print text.read()

filename = "writte.txt"

print "Writing in file %s" % filename

text = open(filename, 'a')

text.write("You ran ex3 program \n")

text.close()


