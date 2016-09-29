xchar = raw_input("enter first charecter : ")
key = int(raw_input("enter your cypher num : "))
cypher = ''
for i in xchar :
	x = ord (i) - key
	if x < 32 :
		print x 
		x = x - 32
		print x 
		x = 126 + x
		print x 
	cypher = cypher + chr(x)
print cypher
