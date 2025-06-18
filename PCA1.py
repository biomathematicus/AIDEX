import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Generate a 3D point cloud centered along a plane with some noise
np.random.seed(42)
n_points = 100
X = np.random.randn(n_points)
Y = 0.5 * X + 0.1 * np.random.randn(n_points)
Z = 0.2 * X + 0.1 * np.random.randn(n_points)
data = np.vstack((X, Y, Z)).T

# Apply PCA
pca = PCA(n_components=3)
pca.fit(data)
components = pca.components_
mean = pca.mean_

# Plot the original point cloud and principal components
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 0], data[:, 1], data[:, 2], alpha=0.6)

# Plot the principal components
for length, vector in zip(pca.explained_variance_, components):
    v = vector * 3 * np.sqrt(length)
    ax.quiver(*mean, *v, color='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Point Cloud with PCA Components')
plt.show()
