## 2. Aplicar Filtros nas Imagens
# Aplicar filtros nas imagens
plt.figure(figsize=(15, 10))
for i in range(num_images_to_display):
    img_path = image_files[i]
    img = cv2.imread(img_path)
    if img is None:
        print(f"Erro: Não foi possível carregar a imagem {img_path}.")
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converter para RGB

    # Aplicar filtro de blur
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

    # Aplicar filtro de detecção de bordas (Canny)
    edges_img = cv2.Canny(img, 100, 200)

    # Exibir imagem original
    plt.subplot(3, num_images_to_display, i + 1)
    plt.imshow(img)
    plt.title("Original")
    plt.axis('off')

    # Exibir imagem com blur
    plt.subplot(3, num_images_to_display, num_images_to_display + i + 1)
    plt.imshow(blurred_img)
    plt.title("Blur")
    plt.axis('off')

    # Exibir imagem com detecção de bordas
    plt.subplot(3, num_images_to_display, 2 * num_images_to_display + i + 1)
    plt.imshow(edges_img, cmap='gray')
    plt.title("Bordas (Canny)")
    plt.axis('off')

plt.suptitle("Aplicação de Filtros nas Imagens", fontsize=16)
plt.show()
