from PIL import Image

def rgb_to_gray(rgb):
    # Conversão de RGB para escala de cinza
    return int(0.2989 * rgb[0] + 0.5870 * rgb[1] + 0.1140 * rgb[2])

def histogram_equa(image_path):
    # Abre a imagem
    image = Image.open(image_path)
    width, height = image.size
    
    # Cria uma nova imagem em escala de cinza
    image_gray = Image.new('L',(width, height))
    
    # Escala de cinza
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            gray_value = rgb_to_gray(pixel)
            image_gray.putpixel((x, y), gray_value)
    
    histogram = [0] * 256
    for y in range(height):
        for x in range(width):
            pixel = image_gray.getpixel((x, y))
            histogram[pixel] += 1
    
    # Calcula a função de distribuição cumulativa (CDF) do histograma
    cdf = [sum(histogram[:i+1]) for i in range(256)]
    
    # equalização
    equalized_image = Image.new('L', (width, height))
    total_pixels = width * height
    for y in range(height):
        for x in range(width):
            pixel = image_gray.getpixel((x, y))
            new_pixel_value = int((cdf[pixel] / total_pixels) * 255)
            equalized_image.putpixel((x, y), new_pixel_value)
    
    return equalized_image

image_path = 'imagem.jpg'

imagem_equalizada = histogram_equa(image_path)

# Salva a imagem para abertura manual
output_image_path = 'imagem_equalizada.jpg'
imagem_equalizada.save(output_image_path)

# Exibe uma mensagem informando o caminho da imagem
print(f"Imagem equalizada salva em: {output_image_path}. Abra manualmente com seu visualizador de imagens preferido.")
