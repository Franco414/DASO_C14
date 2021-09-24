i = int("27")
f=float("3.14")

print("int:")
print(i)
print("float:")
print(f)

s=str(27)
print("s:")
print(s)
s2=str(3.27)
print("s2:")
print(s2)

data = bytearray.fromhex("FFAA0B")
print(data[0]) #255

data = bytearray("0123",encoding="utf-8")
print(data[0]) #48=0x30='0'