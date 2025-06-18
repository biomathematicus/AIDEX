"""
PCA3.py
PCA demonstration using a synthetic spherical mesh with axis alignment 
visualization.

By Juan B. Gutiérrez, Professor of Mathematics 
University of Texas at San Antonio.

License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import open3d as o3d
import numpy as np
from sklearn.decomposition import PCA

# Load a simple 3D teapot mesh
mesh = o3d.geometry.TriangleMesh.create_sphere(radius=1.0).subdivide_midpoint(1)
mesh.compute_vertex_normals()

# Sample sparse points from the mesh surface
pcd = mesh.sample_points_poisson_disk(number_of_points=300)
points = np.asarray(pcd.points)

# Apply PCA
pca = PCA(n_components=3)
pca.fit(points)
components = pca.components_
mean = pca.mean_

# Transform to PCA coordinates
transformed_points = pca.transform(points)

# Create Open3D point clouds
original_pcd = o3d.geometry.PointCloud()
original_pcd.points = o3d.utility.Vector3dVector(points)

pca_pcd = o3d.geometry.PointCloud()
pca_pcd.points = o3d.utility.Vector3dVector(transformed_points)

# Add coordinate axes
axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5, origin=[0, 0, 0])

# Visualize original
print("Original point cloud in native coordinates")
o3d.visualization.draw_geometries([original_pcd, axes])

# Visualize PCA-aligned
print("Point cloud after PCA (aligned to principal axes)")
o3d.visualization.draw_geometries([pca_pcd, axes])
