import math

def vector_sum(A,B):
    t=[0,0,0]
    t[0]=A[0]+B[0]
    t[1]=A[1]+B[1]
    t[2]=A[2]+B[2]
    return t
def vector_product(A,B):
    t=0
    t+=A[0]*B[0]
    t+=A[1]*B[1]
    t+=A[2]*B[2]
    return t
def vector_norm(A):
    t=0
    t+=A[0]*A[0]
    t+=A[1]*A[1]
    t+=A[2]*A[2]
    return "{:.2f}".format(math.sqrt(t))




