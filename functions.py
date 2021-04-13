from numpy import linalg as LA

def cosineSimilarity(A,B):
    numerator=A*B.T
    denominator=LA.norm(A)*LA.norm(B)
    if denominator==0:
        return 0
    else: return numerator/denominator
