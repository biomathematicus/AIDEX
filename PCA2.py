"""
PCA2.py
PCA applied to a 3D bunny mesh using Open3D; compares original and 
PCA-aligned point clouds.

By Juan B. Gutiérrez, Professor of Mathematics
University of Texas at San Antonio.

License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import open3d as o3d
import numpy as np
from sklearn.decomposition import PCA

# Load 3D bunny model as a point cloud 
mesh = o3d.io.read_triangle_mesh(o3d.data.BunnyMesh().path)
mesh.compute_vertex_normals()
points = np.asarray(mesh.vertices)

# Apply PCA
pca = PCA(n_components=3)
pca.fit(points)
components = pca.components_
mean = pca.mean_

# Center and transform points
centered_points = points - mean
transformed_points = pca.transform(points)

# Create Open3D point clouds
original_pcd = o3d.geometry.PointCloud()
original_pcd.points = o3d.utility.Vector3dVector(points)

pca_pcd = o3d.geometry.PointCloud()
pca_pcd.points = o3d.utility.Vector3dVector(transformed_points)

# Coordinate axes (length = 0.05 for visibility)
axes_original = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.05, origin=[0, 0, 0])
axes_pca = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.05, origin=[0, 0, 0])

# Visualize original cloud with axes
print("Original point cloud in native coordinates")
o3d.visualization.draw_geometries([original_pcd, axes_original])

# Visualize PCA-aligned cloud with axes
print("Point cloud after PCA (aligned to principal axes)")
o3d.visualization.draw_geometries([pca_pcd, axes_pca])
