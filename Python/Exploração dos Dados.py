import os
import cv2
import matplotlib.pyplot as plt

# Caminho do dataset
DATA_DIR = '/kaggle/input/ulid25k'  # Ajuste conforme necessário

# Verificar se o diretório existe
if not os.path.exists(DATA_DIR):
    raise FileNotFoundError(f"O diretório {DATA_DIR} não foi encontrado. Verifique o caminho do dataset.")

# Listar todos os arquivos .png no dataset (incluindo subdiretórios)
image_files = []
for root, _, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith('.png'):
            image_files.append(os.path.join(root, file))

# Verificar se há imagens no dataset
print(f"Total de imagens no dataset: {len(image_files)}")
if len(image_files) == 0:
    raise ValueError("Nenhuma imagem foi encontrada no diretório especificado.")

# Exibir algumas imagens de exemplo
num_images_to_display = min(9, len(image_files))  # Exibir no máximo 9 imagens
plt.figure(figsize=(10, 10))
for i in range(num_images_to_display):
    img_path = image_files[i]
    img = cv2.imread(img_path)
    if img is None:
        print(f"Erro: Não foi possível carregar a imagem {img_path}.")
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converter para RGB
    plt.subplot(3, 3, i + 1)
    plt.imshow(img)
    plt.axis('off')
plt.suptitle('Exemplos de Imagens do ULID25k Dataset', fontsize=16)
plt.show()
