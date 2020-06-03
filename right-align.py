
listname=[]
n=input("Enter strings (end with DONE):\n")
maxlen=0
while n!="DONE":
    listname.append(n)
    maxlen=max(maxlen,len(n))
    n=input("")
listnameb=[]
for c in listname:
    t=maxlen-len(c)
    print(" "*t,c)


#print(listname)
#print(maxlen)

