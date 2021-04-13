import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
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

def ConmmunityDetection(user_item_matrix,n_cluster):
    user_average_rating=calculate_user_AverageRatings(user_item_matrix)
    row=len(user_item_matrix)
    col=len(user_item_matrix[0])
    for i in range(1,row):
        for j in range(1,col):
            if user_item_matrix[i][j]==-1:       
                user_item_matrix[i][j]=user_average_rating[i]
    X=user_item_matrix
    kmeans = KMeans(n_clusters=n_cluster, random_state=0).fit(X)
    pca = PCA(n_components=2)
    pca.fit(X)
    x=pca.transform(X)
    
    cluster_result=kmeans.labels_
    plt.scatter(x[:, 0], x[:, 1], c=cluster_result, cmap='viridis')

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    plt.show()

user_item_matrix=np.full((943+1,1682+1),-1) #each row represents a user and each col represents a item, user_item_matrix[i][j]=user i's rating of item j
file = open('ml-100k/u.data', 'r')
Lines = file.readlines()
for line in Lines:
    splits=line.strip().split('\t')
    user_id=int(splits[0])
    item_id=int(splits[1])
    rating=int(splits[2])

    user_item_matrix[user_id][item_id]=rating


ConmmunityDetection(user_item_matrix,19)