"""
Cluster2.py
Interactive K-Means clustering with a slider for number of clusters and 
embedded explanation.

By Juan B. Gutiérrez, Professor of Mathematics 
University of Texas at San Antonio.

License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate 2D points from multiple distributions
n_samples = 300
centers = [(-5, -5), (0, 0), (5, 5)]
X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=1.0, random_state=42)

# Plotting function
def plot_clusters(n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    labels = kmeans.fit_predict(X)
    ax_plot.cla()
    for label in set(labels):
        pts = X[labels == label]
        ax_plot.scatter(pts[:, 0], pts[:, 1], label=f"Cluster {label}")
    ax_plot.set_title(f"K-Means Clustering | Clusters: {n_clusters}")
    ax_plot.legend()
    ax_text.cla()
    explanation = (
        "This plot shows how changing the number of clusters in K-Means affects the grouping of points. "
        "K-Means partitions the dataset into the specified number of clusters by minimizing intra-cluster variance. "
        "As the number of clusters increases, the algorithm assigns points more locally."
    )
    ax_text.text(0, 1, explanation, va='top', wrap=True, fontsize=16)
    ax_text.axis('off')
    fig.canvas.draw_idle()

# Set up the figure and slider
fig, (ax_plot, ax_text) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(bottom=0.25)

initial_clusters = 3
plot_clusters(initial_clusters)

# Create slider in its own axis
ax_slider = plt.axes([0.25, 0.05, 0.5, 0.03])
slider = Slider(ax_slider, 'Clusters', 1, 10, valinit=initial_clusters, valstep=1)

fig.canvas.manager.set_window_title('K-means Clustering')

slider.on_changed(lambda val: plot_clusters(int(val)))
plt.show()
