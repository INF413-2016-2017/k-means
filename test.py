import matplotlib.pyplot as plt

totalDistance = []
cluster = [i for i in range(1,20)]

for nClusters in range(1,20):
    A = GeneralizedLlyod(data, nClusters, D.euclidean, iter_max=5)
    A.run()
    totalDistance.append(A.distMin)

    if nClusters == 1:
        display_points(A.clusters, A.centers)

plt.plot(cluster, totalDistance)
plt.show()