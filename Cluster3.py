import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Initial parameters
n_samples = 300
centers = [(-2, -2), (0, 0), (2, 2)]
initial_std = 0.5

# Generate data with adjustable std
def generate_data(std):
    X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=std, random_state=42)
    return X

# Function to find the optimal number of clusters using silhouette score
def optimal_kmeans(X, max_k=10):
    best_score = -1
    best_k = 2
    best_labels = None
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
        labels = kmeans.fit_predict(X)
        score = silhouette_score(X, labels)
        if score > best_score:
            best_score = score
            best_k = k
            best_labels = labels
    return best_k, best_labels

# Plotting function
def plot_clusters(std):
    global X
    X = generate_data(std)
    best_k, labels = optimal_kmeans(X)
    ax_plot.cla()
    for label in set(labels):
        pts = X[labels == label]
        ax_plot.scatter(pts[:, 0], pts[:, 1], label=f"Cluster {label}")
    ax_plot.set_title(f"Harmonic (Silhouette) Clustering | Optimal Clusters: {best_k}")
    ax_plot.legend()
    ax_text.cla()
    explanation = (
        "This plot shows clustering using an automatic method to select the number of clusters. "
        "Harmonic clustering here refers to using silhouette analysis to find the optimal partitioning. "
        "It selects the number of clusters that maximizes how well-separated and compact the clusters are.\n\n"
        "Use the slider below to adjust the standard deviation of the data distributions. "
        "Greater overlap between clusters can make it harder to determine the optimal number."
    )
    ax_text.text(0, 1, explanation, va='top', wrap=True, fontsize=16)
    ax_text.axis('off')
    fig.canvas.draw_idle()

# Set up the figure
fig, (ax_plot, ax_text) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(bottom=0.25)

X = generate_data(initial_std)
plot_clusters(initial_std)

# Create slider for cluster_std
ax_slider = plt.axes([0.25, 0.05, 0.5, 0.03])
slider = Slider(ax_slider, 'Cluster Std', 0.5, 5.0, valinit=initial_std)
slider.on_changed(plot_clusters)

fig.canvas.manager.set_window_title('Harmonic Clustering')

plt.show()
