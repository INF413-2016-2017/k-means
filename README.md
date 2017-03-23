Use instructions
----------------
Install the **distance** package, for instance using pip: _pip install distance_.  
To use the algorithms on words instead of points, use the option dataType='points' 
or dataType='words' in the instantiation of the class.  
In the file main.py, choose the desired parameters.  
The programs currently work only on _python 2.7_  


Notations
---------
c is the list of chosen centers: c[i] returns the coordinates of the center i.  
C is the list of points in the cluster k. The center is included in the list.  


Archive name
------------
TP1_Gardin_Garet_INF413_2016_2017_A


Todo
----
-Write data back to files: remove whitespaces.  
-Use numpy instead of list/tuples.  
-Bibliographie  
-Faire des recherches  
-Revoir les notations: s'aligner sur l'enoncé  
-Choix de la distance.
-Choix des centres initiaux (voir les pdf)  
-Choix du critère d'arrêt  
-Choix du nombre de centres (à voir, cela peut dépendre de l'utilisation)  
-Study complexity  
-Closing file after write: error.  
-Add command line args  
-Cluster size and number of iterations.  
-Display different iterations.  
-Add more data input.  
-Add ponderation for euclidean distance.  
