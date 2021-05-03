import numpy as np
from functions import *
from numpy import linalg as LA
from tqdm import tqdm
def sort_dict(dict):
    dict=sorted(dict.items(), key=lambda x:x[1],reverse=True)   
    return dict

def calculate_user_AverageRatings(user_item_matrix):
    user_avg_rating={}
    row=len(user_item_matrix)
    col=len(user_item_matrix[0])
    for i in range(1,row):
        total=0
        cnt=0
        for j in range(1,col):
            if user_item_matrix[i][j]!=-1:
                total+=user_item_matrix[i][j]
                cnt+=1
        user_avg_rating[i]=total/cnt
    return user_avg_rating

def calculate_user_Similarity(user_item_matrix,user_id,item_id):
    row=len(user_item_matrix)
    col=len(user_item_matrix[0])
    sim_dict={}
    compare_index=[] # col that will be used to calculate similarity
    sorted_sim_dictionary={}
    for j in range(1,col):
        if j!=item_id and user_item_matrix[user_id][j]!=-1:
            compare_index.append(j)

    for i in range(1,row):
        if i==user_id:
            continue
        
        sum=0
        sqrt_1=0
        sqrt_2=0
        v1=[]
        v2=[]
        for j in compare_index:
            if user_item_matrix[i][j]!=-1:
                v1.append(user_item_matrix[i][j])
                v2.append(user_item_matrix[user_id][j])
        v1=np.array(v1)
        v2=np.array(v2)
        if len(v1)==0:
            continue
        sum=np.dot(v1,v2)
        sqrt_1=LA.norm(v1)
        sqrt_2=LA.norm(v2)
            
        
        sim_score=sum/(sqrt_1*sqrt_2)
        sim_dict[i]=sim_score
        

    dict=sort_dict(sim_dict)
    

    for each in dict:
        sorted_sim_dictionary[each[0]]=each[1]

    return sorted_sim_dictionary

def get_TopK_neighbor_index(sorted_sim_dict,neighbor_size):
    cnt=1
    top_k_neighbor_index=[]
    for each in sorted_sim_dict:
        if cnt>neighbor_size:
            break
        cnt+=1      
        top_k_neighbor_index.append(each)
    return top_k_neighbor_index


def user_based_CF(user_item_matrix,neighbor_size,user_id,item_id,user_avg_rating_dict):
    
    sorted_sim_dict=calculate_user_Similarity(user_item_matrix,user_id,item_id)
    if len(sorted_sim_dict)==0:
        return -1
    top_k_neighbor_index=get_TopK_neighbor_index(sorted_sim_dict,neighbor_size)

    rating=user_avg_rating_dict[user_id]
    sim_sum=0
    for index in top_k_neighbor_index:
        sim_sum+=sorted_sim_dict[index]
    
    for index in top_k_neighbor_index:
        if user_item_matrix[user_id][item_id]!=-1:
            score=sorted_sim_dict[index]*(user_item_matrix[user_id][item_id]-user_avg_rating_dict[index])/sim_sum
            rating+=score
    #print("rating of user_id="+str(user_id)+" to item_id="+str(item_id)+" is "+str(rating))
    return rating

def user_based_Model_Test(user_item_matrix,neighbor_size):
    truth=[]
    prediction=[]
    row=len(user_item_matrix)
    col=len(user_item_matrix[0])
    user_avg_rating_dict=calculate_user_AverageRatings(user_item_matrix)
    for i in tqdm(range(1,row)):
        for j in range(col):
            if user_item_matrix[i][j]!=-1:
                pred=user_based_CF(user_item_matrix,neighbor_size,i,j,user_avg_rating_dict)
                if pred==-1:
                    continue
                truth.append(user_item_matrix[i][j])     
                prediction.append(pred)
    RMSE=RootMeanSquareError(truth,prediction)
    print("RMSE="+str(RMSE))
