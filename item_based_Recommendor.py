from numpy import *
from functions import *
from numpy import linalg as LA
from tqdm import tqdm
import numpy as np
def sort_dict(dict):
    dict=sorted(dict.items(), key=lambda x:x[1],reverse=True)   
    return dict
def calculate_item_AverageRatings(item_user_matrix):
    item_avg_rating={}
    row=len(item_user_matrix)
    col=len(item_user_matrix[0])
    for i in range(1,row):
        total=0
        cnt=0
        for j in range(1,col):
            if item_user_matrix[i][j]!=-1:
                total+=item_user_matrix[i][j]
                cnt+=1
        item_avg_rating[i]=total/cnt
    return item_avg_rating

def get_TopK_neighbor_index(sorted_sim_dict,neighbor_size):
    cnt=1
    top_k_neighbor_index=[]
    for each in sorted_sim_dict:
        if cnt>neighbor_size:
            break
        cnt+=1      
        top_k_neighbor_index.append(each)
    return top_k_neighbor_index

def calculate_item_Similarity(item_user_matrix,user_id,item_id):
    row=len(item_user_matrix)
    col=len(item_user_matrix[0])
    sim_dict={}
    compare_index=[] # col that will be used to calculate similarity
    sorted_sim_dictionary={}
    for j in range(1,col):
        if j!=user_id and item_user_matrix[item_id][j]!=-1:
            compare_index.append(j)

    for i in range(1,row):
        if i==item_id:
            continue
        
        sum=0
        sqrt_1=0
        sqrt_2=0
        v1=[]
        v2=[]
        for j in compare_index:
            if item_user_matrix[i][j]!=-1 :
                v1.append(item_user_matrix[i][j])
                v2.append(item_user_matrix[item_id][j])
                
        sum=np.dot(v1,v2)
        sqrt_1=LA.norm(v1)
        sqrt_2=LA.norm(v2)
        v1=np.array(v1)
        v2=np.array(v2)
        if len(v1)==0:
            continue
        
        sim_score=sum/np.sqrt(sqrt_1*sqrt_2)
        sim_dict[i]=sim_score
        
    dict=sort_dict(sim_dict)
    

    for each in dict:
        sorted_sim_dictionary[each[0]]=each[1]

    return sorted_sim_dictionary

def item_based_CF(item_user_matrix,neighbor_size,item_id,user_id,item_avg_rating_dict):
    
    sorted_sim_dict=calculate_item_Similarity(item_user_matrix,user_id,item_id)
    top_k_neighbor_index=get_TopK_neighbor_index(sorted_sim_dict,neighbor_size)

    rating=item_avg_rating_dict[item_id]
    sim_sum=0
    for index in top_k_neighbor_index:
        sim_sum+=sorted_sim_dict[index]
    
    for index in top_k_neighbor_index:
        if item_user_matrix[item_id][user_id]!=-1:
            score=sorted_sim_dict[index]*(item_user_matrix[item_id][user_id]-item_avg_rating_dict[index])/sim_sum
            rating+=score
    #print("rating of user_id="+str(user_id)+" to item_id="+str(item_id)+" is "+str(rating))
    return rating

def item_based_Model_Test(item_user_matrix,neighbor_size):
    item_avg_rating_dict=calculate_item_AverageRatings(item_user_matrix)
    truth=[]
    prediction=[]
    row=len(item_user_matrix)
    col=len(item_user_matrix[0])
   
    for i in tqdm(range(944,row)):
        for j in range(col):
            if item_user_matrix[i][j]!=-1:
                truth.append(item_user_matrix[i][j])
                pred=item_based_CF(item_user_matrix,neighbor_size,i,j,item_avg_rating_dict)
                prediction.append(pred)
    RMSE=RootMeanSquareError(truth,prediction)
    print("RMSE="+str(RMSE))
