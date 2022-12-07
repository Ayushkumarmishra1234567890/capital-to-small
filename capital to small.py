#change capital to small and small to capital
a=input("Give: ")
b=ord(a)
if(b<97):
    b=b+32
else:
    b=b-32
print(chr(b))
