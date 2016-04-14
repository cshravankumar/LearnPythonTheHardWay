#Shravan Kumar Chandrasekaran
#sc3940@columbia.edu
#Exercise 3

######################################
#Importing Libraries
from subprocess import call
from sys import argv
from os.path import exists
#####################################

script, from_file, to_file = argv

print script
#print filename
print from_file
print to_file

print "Copying %s to %s" %(from_file, to_file)

print "Checking if %s file exists..." %from_file

print "%s" %exists(from_file)

print "Checking if %s file exists..." %to_file

print "%s" %exists(to_file)

if(exists(from_file)):

	from_file_instance = open(from_file)
	data_from_file = from_file_instance.read()
	
	if(exists(to_file)):
		
		to_file_instance = open(to_file,'w')
		to_file_instance.write(data_from_file)
		from_file_instance.close()
		to_file_instance.close()

	else:
		print "%s file doesn't exist" %to_file
		form_file_instance.close()
else:
	print "%s does not exist" %from_file

#END
