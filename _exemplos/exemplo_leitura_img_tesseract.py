from PIL import Image
import pytesseract

# Configurar o caminho do executável do Tesseract (necessário apenas no Windows)
# Substitua pelo caminho correto no seu sistema
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Caminho da imagem que será analisada
imagem_caminho = "teste.png"  # Substitua pelo caminho da sua imagem

# Abrir a imagem com Pillow
imagem = Image.open(imagem_caminho)

# Usar o Tesseract para extrair texto
texto = pytesseract.image_to_string(imagem, lang='por')

# Exibir o texto extraído
print("Texto extraído da imagem:")
print(texto)

# Salvar o texto em um arquivo
with open("texto_extraido.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)
    print("Texto salvo no arquivo 'texto_extraido.txt'")
