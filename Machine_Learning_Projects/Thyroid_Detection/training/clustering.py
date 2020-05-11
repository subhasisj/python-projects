import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kneed import KneeLocator
import streamlit as st
import pandas as pd

class KmeansClustering:
    def __init__(self,logger,data):
        self._logger = logger
        self._data = data
        self.n_clusters = None

    def find_clusters_using_elbow_plot(self):
        
        self._logger.log('Clustering: Finding number of clusters using Elbow plot')

        wcss=[] # initializing an empty list
        try:
            for i in range (1,11):
                kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42) # initializing the KMeans object
                kmeans.fit(self._data) # fitting the data to the KMeans Algorithm
                wcss.append(kmeans.inertia_)

            wcss_df = pd.DataFrame.from_dict({'k-value':range(1,11), 'wcss':wcss})
            wcss_df.set_index('k-value',inplace=True)
            st.line_chart(wcss_df)
            kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
            self._logger.log(f'Clustering: Number of Clusters found: {str(kn.knee)}')
            self.n_clusters = kn.knee
            return self.n_clusters
        except Exception as e:
            self._logger.log(f'Clustering: Exception occured: {str(e)}','critical')

    def assign_clusters_to_data(self, data):

        self._logger.log(f'Clustering: Initializing Kmeans with {self.n_clusters}')
        try:
            self.kmeans = KMeans(n_clusters=self.n_clusters, init='k-means++', random_state=42)
            #self.data = self.data[~self.data.isin([np.nan, np.inf, -np.inf]).any(1)]
            y_kmeans=self.kmeans.fit_predict(data) #  divide data into clusters

            # self.save_model = self.file_op.save_model(self.kmeans, 'KMeans') # saving the KMeans model to directory

            data['Cluster']=y_kmeans  # create a new column in dataset for storing the cluster information
            self._logger.log(f'Clustering: Clusters assigned to data successfully')
            return data
        except Exception as e:
            self._logger.log(f'Clustering: Exception occured while clustering data - {str(e)}','critical')
            raise Exception()


