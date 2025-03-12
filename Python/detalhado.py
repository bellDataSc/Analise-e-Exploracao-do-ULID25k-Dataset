## Essas duas análises adicionam um nível mais detalhado¶
## 🚀 Distribuição de Cores Dominantes
## Utiliza o algoritmo K-means para extrair as cores dominantes das imagens, permitindo uma análise da paleta de cores predominante no dataset.

## 🚀 Análise de Bordas e Detecção de Contornos
## Aplica a detecção de bordas (Canny) para examinar a complexidade visual das imagens, ajudando a entender a riqueza de detalhes das paisagens.

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Caminho do dataset
DATA_DIR = '/kaggle/input/ulid25k'  # Ajuste conforme necessário

# Listar arquivos .png no dataset
image_files = []
for root, _, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith('.png'):
            image_files.append(os.path.join(root, file))

# Função para extrair cores dominantes usando K-Means
def get_dominant_colors(image_path, k=5):
    img = cv2.imread(image_path)
    if img is None:
        return None
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(img)
    return kmeans.cluster_centers_.astype(int)

# Analisar cores das primeiras 10 imagens
dominant_colors = []
num_images = min(10, len(image_files))
for i in range(num_images):
    colors = get_dominant_colors(image_files[i])
    if colors is not None:
        dominant_colors.append(colors)

# Exibir cores dominantes
fig, axes = plt.subplots(num_images, 1, figsize=(8, num_images * 2))
for i, colors in enumerate(dominant_colors):
    axes[i].imshow([colors])
    axes[i].axis('off')
    axes[i].set_title(f'Imagem {i + 1}')
plt.suptitle('Cores Dominantes nas Imagens', fontsize=16)
plt.show()

# Função para aplicar detecção de bordas Canny
def detect_edges(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    edges = cv2.Canny(img, 100, 200)
    return edges

# Aplicar detecção de bordas nas primeiras 9 imagens
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
for i in range(min(9, len(image_files))):
    edges = detect_edges(image_files[i])
    if edges is not None:
        row, col = divmod(i, 3)
        axes[row, col].imshow(edges, cmap='gray')
        axes[row, col].axis('off')
plt.suptitle('Detecção de Bordas nas Imagens', fontsize=16)
plt.show()
