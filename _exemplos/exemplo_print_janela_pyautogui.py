import pyautogui
import pygetwindow as gw
from PIL import ImageGrab  # Para capturar uma região específica da tela
import cv2
import numpy as np

# Função para capturar a janela específica
def capturar_janela(nome_janela, arquivo_screenshot="janela_screenshot.png"):
    # Obter a janela pelo título
    janela = gw.getWindowsWithTitle(nome_janela)
    if not janela:
        print(f"Janela '{nome_janela}' não encontrada!")
        return None
    janela = janela[0]  # Seleciona a primeira janela encontrada

    # Ativar a janela (trazê-la para o topo)
    janela.activate()

    # Aguardar a janela
    pyautogui.sleep(1)  # Aguardar 1 segundo para a janela ficar visível

    # Pegar as dimensões da janela
    left, top, right, bottom = janela.left, janela.top, janela.right, janela.bottom
    print(f"Capturando janela '{nome_janela}' com dimensões: ({left}, {top}, {right}, {bottom})")

    # Capturar a área da janela usando ImageGrab
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save(arquivo_screenshot)
    print(f"Screenshot salvo como: {arquivo_screenshot}")
    return arquivo_screenshot

# Função para verificar o objeto na captura da janela
def verificar_objeto_em_janela(nome_janela, objeto, arquivo_screenshot="janela_screenshot.png"):
    # Capturar a janela
    screenshot = capturar_janela(nome_janela, arquivo_screenshot)
    if screenshot is None:
        return False

    # Verificar o objeto
    img_grande = cv2.imread(screenshot)  # Imagem capturada
    img_pequena = cv2.imread(objeto)    # Imagem do objeto a ser encontrado

    # Converter para escala de cinza
    img_grande_gray = cv2.cvtColor(img_grande, cv2.COLOR_BGR2GRAY)
    img_pequena_gray = cv2.cvtColor(img_pequena, cv2.COLOR_BGR2GRAY)

    # Match Template para localizar o objeto
    resultado = cv2.matchTemplate(img_grande_gray, img_pequena_gray, cv2.TM_CCOEFF_NORMED)
    _, max_valor, _, max_pos = cv2.minMaxLoc(resultado)

    # Se o valor máximo for maior que o limiar, o objeto foi encontrado
    limiar = 0.8
    if max_valor >= limiar:
        print(f"Objeto encontrado na janela '{nome_janela}'! Coordenadas: {max_pos}")
        # Clicar no objeto
        x, y = max_pos
        pyautogui.click(x + img_pequena.shape[1] // 2, y + img_pequena.shape[0] // 2)  # Clicar no centro do objeto
        print("Clicado no objeto na janela!")  # Adicionar aqui a ação desejada após o clique
        return True
    else:
        print(f"Objeto não encontrado na janela '{nome_janela}'.")
        return False

if __name__ == "__main__":
    nome_janela = "Visual Studio Code"  # Substitua pelo nome da janela desejada
    objeto = "validador.png"           # Caminho da imagem do objeto a ser localizado
    verificar_objeto_em_janela(nome_janela, objeto)

input('Espera')