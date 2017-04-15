Use instructions
----------------
Install the **distance** package, for instance using pip: _pip install distance_.  
To use the algorithms on words instead of points, use the option dataType='points' 
or dataType='words' in the instantiation of the class.  
In the file main files, choose the desired parameters (number of data, number of clusters).
The programs currently work only on _python 2.7_

_main_points.py_ execute tout à tour trois variantes de l'algorithme k-means.

_main_words.py_ execute l'algorithme avec une liste de mots.

_g-means_points_ execute l'algorithme G-means sur des points.

_test_gaussian.py_ permet de visualiser l'efficacité de la détection des distributions gaussiennes.


Notations
---------
_centers_: list of chosen centers: _centers[i]_ returns the coordinates of the center _i_.
_clusters_: list of points in the cluster _k_. The center is included in the list.


Archive name
------------
TP1_Gardin_Garet_INF413_2016_2017_A
