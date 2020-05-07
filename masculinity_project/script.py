# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:35:17 2020

@author: G&S
"""
import pandas as pd
# from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

""" Load data """

survey = pd.read_csv("masculinity.csv")

''' Selelct rows the rows we want to work on and convert
 responses into numerical data.'''

cols_to_map = ["q0007_0001", "q0007_0002", "q0007_0003", "q0007_0004",
       "q0007_0005", "q0007_0006", "q0007_0007", "q0007_0008", "q0007_0009",
       "q0007_0010", "q0007_0011"]

for col in cols_to_map:
    survey[col] = survey[col].map({'Never, and not open to it': 0,
                           'Never, but open to it': 1,
                           'Rarely': 2,
                           'Sometimes': 3,
                           'Often': 4
                            })
   
    
    
relevant_cols = ["q0007_0001", "q0007_0002", "q0007_0003", "q0007_0004",
        "q0007_0005", "q0007_0008", "q0007_0009"]
rows_to_cluster = survey.dropna(subset=relevant_cols) # Drop null values

'''Build the KMeans Model '''

classifier = KMeans(n_clusters = 2)
classifier.fit(rows_to_cluster[relevant_cols])
# print(classifier.cluster_centers_)
# print(classifier.labels_)


""" Seperate the cluster members"""

cluster_zero_indices = []
cluster_one_indices = []

for i in range(len(classifier.labels_)):
    if classifier.labels_[i] == 0:
        cluster_zero_indices.append(i)
    else:
        cluster_one_indices.append(i)

# print(cluster_zero_indices)
'''Look at some stats about these two clusters.'''

cluster_zero_df = rows_to_cluster.iloc[cluster_zero_indices]
cluster_one_df = rows_to_cluster.iloc[cluster_one_indices]

print(cluster_zero_df['educ4'].value_counts()/len(cluster_zero_df))
print(cluster_one_df['educ4'].value_counts()/len(cluster_one_df))



                                
                                
                                
                                
                                
                                
                                
                                
                                
                                