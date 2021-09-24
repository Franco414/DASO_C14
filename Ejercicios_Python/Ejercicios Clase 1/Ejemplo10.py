s = "\u00D1"
print(s)
ba= s.encode("utf-8")
print(ba)
s2= ba.decode("utf-8")
print(s2)