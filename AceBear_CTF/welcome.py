import itertools

chall = "172d330d21283133037c65101220703c187a3b1033202f24092c33103021261721273821773b3e".decode("hex")
clear = "AceBear{"

#print [(ord(i) - ord(j)) for i,j in zip(chall[:len(clear)], clear)]

key = "".join( chr(ord(a)^ord(b)) for a,b in zip(chall[:len(clear)], clear) )

print key

print "".join( chr(ord(a)^ord(b)) for a,b in zip(chall, itertools.cycle(key)) )
