import numpy as np
from functions import *
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

    for j in range(1,col):
        if j!=item_id and user_item_matrix[user_id][j]!=-1:
            compare_index.append(j)

    for i in range(1,row):
        if i==user_id:
            continue
        
        sum=0
        sqrt_1=0
        sqrt_2=0
        for j in compare_index:
            if user_item_matrix[i][j]!=-1:
                sum+=user_item_matrix[i][j]*user_item_matrix[user_id][j]
                sqrt_1+=user_item_matrix[i][j]**2
                sqrt_2+=user_item_matrix[user_id][j]**2
        if sqrt_1*sqrt_2!=0:
            sim_score=sum/np.sqrt(sqrt_1*sqrt_2)
            sim_dict[i]=sim_score
        else:
            sim_dict[i]=0

    dict=sort_dict(sim_dict)
    sorted_sim_dictionary={}

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


def user_based_CF(user_item_matrix,neighbor_size,user_id,item_id):
    user_avg_rating_dict=calculate_user_AverageRatings(user_item_matrix)
    sorted_sim_dict=calculate_user_Similarity(user_item_matrix,user_id,item_id)
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

    for i in range(row):
        for j in range(col):
            if user_item_matrix[i][j]!=-1:
                truth.append(user_item_matrix[i][j])
                pred=user_based_CF(user_item_matrix,neighbor_size,i,j)
                prediction.append(pred)
    RMSE=RootMeanSquareError(truth,prediction)
    print("RMSE="+str(RMSE))
