#Outras maneiras de visualizar as imagens e realizar análises¶
#1. Visualizar Imagens em Tons de Cinza
# Exibir imagens originais e em tons de cinza


plt.figure(figsize=(15, 10))
for i in range(num_images_to_display):
    img_path = image_files[i]
    img = cv2.imread(img_path)
    if img is None:
        print(f"Erro: Não foi possível carregar a imagem {img_path}.")
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converter para RGB
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Converter para tons de cinza

    # Exibir imagem original
    plt.subplot(2, num_images_to_display, i + 1)
    plt.imshow(img)
    plt.title("Original")
    plt.axis('off')

    # Exibir imagem em tons de cinza
    plt.subplot(2, num_images_to_display, num_images_to_display + i + 1)
    plt.imshow(gray_img, cmap='gray')
    plt.title("Tons de Cinza")
    plt.axis('off')

plt.suptitle("Imagens Originais vs Tons de Cinza", fontsize=16)
plt.show()
