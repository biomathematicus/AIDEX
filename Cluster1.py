"""
Cluster1.py
Distance-based clustering visualization with adjustable threshold and 
explanatory text panel.

By Juan B. Gutiérrez, Professor of Mathematics 
University of Texas at San Antonio.

License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.datasets import make_blobs
from scipy.spatial.distance import pdist, squareform

# Generate 2D points from multiple distributions
n_samples = 300
centers = [(-5, -5), (0, 0), (5, 5)]
X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=1.0, random_state=42)

# Function to perform simple distance-based clustering
def cluster_by_distance(X, threshold):
    distances = squareform(pdist(X))
    n = len(X)
    labels = -np.ones(n, dtype=int)
    cluster_id = 0

    for i in range(n):
        if labels[i] == -1:
            labels[i] = cluster_id
            to_visit = [i]
            while to_visit:
                current = to_visit.pop()
                neighbors = np.where((distances[current] < threshold) & (labels == -1))[0]
                labels[neighbors] = cluster_id
                to_visit.extend(neighbors.tolist())
            cluster_id += 1
    return labels

# Plotting function
def plot_clusters(threshold):
    labels = cluster_by_distance(X, threshold)
    n_clusters = len(set(labels))
    ax_plot.cla()
    for label in set(labels):
        pts = X[labels == label]
        ax_plot.scatter(pts[:, 0], pts[:, 1], label=f"Cluster {label}")
    ax_plot.set_title(f"Threshold: {threshold:.2f} | Clusters: {n_clusters}")
    ax_plot.legend()
    ax_text.cla()
    explanation = (
        "This plot shows how changing the clustering threshold affects the grouping of points. "
        "Clusters are formed by connecting points that are closer than the threshold distance. "
        "As the threshold increases, more points are grouped together, reducing the number of clusters."
    )
    ax_text.text(0, 1, explanation, va='top', wrap=True, fontsize=18)
    ax_text.axis('off')
    fig.canvas.draw_idle()

# Set up the figure and slider
fig, (ax_plot, ax_text) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(bottom=0.25)

initial_threshold = 1.5
plot_clusters(initial_threshold)

# Create slider in its own axis
ax_slider = plt.axes([0.25, 0.05, 0.5, 0.03])
slider = Slider(ax_slider, 'Threshold', 0.1, 2.0, valinit=initial_threshold)

fig.canvas.manager.set_window_title('Naive Clustering')

slider.on_changed(plot_clusters)
plt.show()
