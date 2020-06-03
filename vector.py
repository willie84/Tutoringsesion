
import vectormaths

Ainpu=raw_input("Enter vector A: \n").split(" ")
Binpu=raw_input("Enter vector B: \n").split(" ")
A=[0,0,0]
B=[0,0,0]
A[0]=eval(Ainpu[0])
A[1]=eval(Ainpu[1])
A[2]=eval(Ainpu[2])
B[0]=eval(Binpu[0])
B[1]=eval(Binpu[1])
B[2]=eval(Binpu[2])

print(A)

D=raw_input("Select a calculation to perform. Enter '+', '.' or '|':")

if D=="+":
    print("A+B = ",vectormaths.vector_sum(A,B))
elif D==".":
     print("A.B = ",vectormaths.vector_product(A,B))
elif D=="|":
     print("|A| = ",vectormaths.vector_norm(A))
     print("|B| = ",vectormaths.vector_norm(B))
else:
    print("Selection not recognised.")

