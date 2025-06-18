# AIDEX

**AIDEX** (AI and Data EXamples) is a collection of compact, practical [Python](https://www.python.org/) and [MATLAB](https://www.mathworks.com/) (compatible with open-source [Octave](https://www.octave.org/)) programs.  Examples are developed in MATLAB/[Octave](https://www.octave.org/) when it is important to look at equations; for all else, examples are in Python.  

Examples in AIDEX illustrate foundational and advanced concepts in mathematics, data science, machine learning, and artificial intelligence. Each example is self-contained and visual, designed to be useful for education, experimentation, and demonstration. 

---

## 📁 Contents

### 🧮 Calculus - Interpretation of Derivatives and Minimization
- [**Example_A1.py**](Example_A1.py)  
  Animated sigmoid-like function with tangent and derivative speedometer.
- [**Example_A2.py**](Example_A2.py)  
  Slider-controlled visualization of function and its derivative, including tangents.
- [**Example_A3.py**](Example_A3.py)  
  Combines function, derivative, and polar speedometer in one dashboard.

### 🔢 PCA and Dimensionality Reduction
- [**PCA.m**](PCA.m)  
  Implements PCA step-by-step in MATLAB without libraries. Shows 3D data, mean-centering, scatter matrix, eigendecomposition, projection onto principal components, and a Pareto plot of explained variance.
- [**PCA1.py**](PCA1.py)  
  Demonstrates PCA on synthetic 3D data with visualization of principal axes in 3D space.
- [**PCA2.py**](PCA2.py)  
  Applies PCA to a 3D bunny mesh using Open3D. Compares original and PCA-aligned point clouds.
- [**PCA3.py**](PCA3.py)  
  Similar to PCA2 but uses a synthetic spherical object to visualize PCA rotation effects.

### 📊 Clustering
- [**Cluster1.py**](Cluster1.py)  
  Distance-based clustering with an interactive threshold slider and explanation panel.
- [**Cluster2.py**](Cluster2.py)  
  K-Means clustering with an adjustable number of clusters and real-time plot updates.
- [**Cluster3.py**](Cluster3.py)  
  Uses silhouette scores to determine the optimal number of clusters dynamically based on overlap, with a standard deviation slider.

### 🧠 Gradient Descent and Learning
- [**Example_B.py**](Example_B.py)  
  Visual metaphor of gradient descent as a ball in a well, with step-by-step algebra shown.
- [**Example_C.py**](Example_C.py)  
  Illustrates convergence of a single weight using gradient descent in supervised learning.

### 📈 Adaptive Linear Mapping
- [**Example_D.py**](Example_D.py)  
  High-dimensional matrix learning with sliders to adjust input/output dimensions and iteration count.

---

## 🧭 Purpose

AIDEX is designed for:
- Instructors needing concise, visual examples for lectures or labs.
- Students exploring key algorithms interactively.
- Practitioners prototyping educational tools or demonstrations.

---

## 📦 Requirements

Most examples require:
- `numpy`, `matplotlib`, `scikit-learn`
- `open3d` (for 3D visualization in PCA2 and PCA3)

Install dependencies with:
```bash
pip install numpy matplotlib scikit-learn open3d
