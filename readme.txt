1.We implemented several methods to predict missing value

2.Create user and item classes in user.py and item.py

3.Memory based recommendation system:
    3.1 user-based_Recommendor.py 
    3.2 item_based_Recommendor.py 

4.Model based recommendation systm:
    4.1 Simple Matrix factorization method in main.ipynb section 8 (http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/)
        4.1.1 Initialize the missing value to be 0
        4.1.2 Initialize the missing value to be global mean
        4.1.3 Initialize the missing value to be user i's average rating
    4.2 SVD in main.ipynb section 6 (Surprise package: http://surpriselib.com/)
    4.3 SVD++ in main.ipynb section 7 (Suprise package: http://surpriselib.com/)

5.Clustering methods
    5.1 Coummunity_detection.py (cluster users in 19 groups)
        5.1.1 K means algorithm

6.Loss function:
    6.1 RMSD loss in functions.py
    6.2 Cosine Similarity in functions.py

7.Data:
Movielens 100 k (https://grouplens.org/datasets/movielens/)

8.Test results
test results are shown in main.ipynb