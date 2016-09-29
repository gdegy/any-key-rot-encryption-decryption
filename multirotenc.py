xchar = raw_input("enter first charecter : ")
key = int(raw_input("enter your cypher num : "))
cypher = ''
for i in xchar :
	x = ord (i) + key
	print x
	if x > 126 :
		x = x - 126
		print x
		x = x + 32 
		print x
	cypher = cypher + chr (x)
print cypher
