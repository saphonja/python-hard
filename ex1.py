name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "He's %d kgs heavy." % (weight * 0.453)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get is exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)
