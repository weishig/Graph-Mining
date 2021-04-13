from numpy import linalg as LA
import numpy as np
def cosineSimilarity(A,B):
    numerator=A*B.T
    denominator=LA.norm(A)*LA.norm(B)
    if denominator==0:
        return 0
    else: return numerator/denominator

def RootMeanSquareError(truth,prediction):
    sum=0
    N=len(truth)
    if len(truth)!=len(prediction):
        print("length of truth vector does not match with that of prediciton")
        return False
    for i in range(N):
        sum+=(truth[i]-prediction[i])**2
    
    return np.sqrt(sum/N)
