import numpy as np
import os
from clustering.base_clustering import BaseClustering

tensor_kmeans   = np.load(f"../../results/experiment/KMeansEngine/labels_tensor_KMeansEngine.npy")
tensor_gmm      = np.load(f"../../results/experiment/KMedoidsEngine/labels_tensor_KMedoidsEngine.npy")

ari_mean_per_k, ari_std_per_k = BaseClustering.cross_method_ari(tensor_kmeans, tensor_gmm)
print(ari_mean_per_k)
