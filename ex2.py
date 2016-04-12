#Shravan Kumar Chandrasekaran
#sc3940@columbia.edu
#Exercise 2

#This is a Comment.
#haha
x = 5
print "Don't",x,"waste"
print "Hey %d there." %5

#####################################

my_name = '@ShravanKumar'
my_age = 26 # not a lie
my_height = 70 # inches
my_weight = 140 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'
######################################
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
#######################################
types_of_People = 2
x = "There are %d types of people" % types_of_People
y = " NYC is a big city. %r" %x
z = " NYC is a big city. %r"
a = " I love NYC" 
print y
print z  % x
print "." * 20
print z %x,
print a
#######################################
formatter = "%r %r %r %r"
print formatter % ("This", "is", "pretty", "cool") 
print formatter % (2<3, 3>2, 4/2, 1+2) 
print formatter % (formatter, formatter, formatter, formatter) 

#######################################

days = "Mon Tue Wed Thu Fri Sat Sun"
Months = "Jan\nFeb\nMar\nApr"

print "These are the days of the week %s" % days
print "These are the days of the week" , days
print "These are the months until now" , Months
print """
Ohh.. this is pretty cool
the \""" kinda works man
"""
######################################

print "How you doing today?"
Var = raw_input()
print "You just said" , Var

print "..So how old are you?"
Age = int(raw_input())
print "So you're %d years old, eh?" %Age



#End
