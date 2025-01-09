import ctypes
import time
import pyautogui # type: ignore
import pygetwindow as gw # type: ignore
from PIL import ImageGrab, Image # type: ignore
import cv2 # type: ignore
import numpy as np # type: ignore
import pytesseract # type: ignore
import keyboard # type: ignore
import random # type: ignore

# Ajuste o caminho do Tesseract, se necessário
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

nome_janela = "РokеMМO"

# Variáveis globais para as coordenadas da janela
left = 0
top = 0
right = 0
bottom = 0

leppa = 0
pokes = 0

def mover_para_cima():
    keyboard.press('w')
    time.sleep(1.5)
    keyboard.release('w')
    print("Andou para cima")

def mover_para_baixo():
    keyboard.press('s')
    time.sleep(1.5)
    keyboard.release('s')
    print("Andou para baixo")

def movimentacao():
    """
    Realiza movimentação aleatória na janela "PokеMMO".
    """
    mover_para_cima()
    mover_para_baixo()
    
    captura_batalha()

def captura_batalha():
    capturar_janela("validador.png")
    imagem_caminho = "validador.png"
    imagem_botao   = "apenas_1.png"

    # Carregar a imagem 'validador.png'
    imagem_principal = cv2.imread(imagem_caminho)

    if imagem_principal is None:
        print("Não foi possível carregar validador.png")
        return

    # Carregar a imagem do botão
    img_botao = cv2.imread(imagem_botao)
    if img_botao is None:
        print("Não foi possível carregar apenas_1.png")
        return

    # Localiza o 'botão' na imagem principal
    resultado = cv2.matchTemplate(imagem_principal, img_botao, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(resultado)

    
    if max_val > 0.8:
        print("Encontrou batalha!")
        time.sleep(4)
        batalha()  # Função que lida com a batalha
    else:
        print("Não encontrou batalha.")
        time.sleep(1.4)
        pyautogui.moveTo(1450, 900)
        pyautogui.click()
        movimentacao()  # Função que realiza a movimentação
    

def capturar_janela(arquivo_screenshot="janela_screenshot.png"):
    """
    Captura a janela especificada pelo nome_janela e salva o screenshot completo
    em arquivo_screenshot, usando as variáveis globais (left, top, right, bottom).
    Retorna: (arquivo_screenshot, (left, top, right, bottom))
    """
    global left, top, right, bottom
    print(f"Capturando janela '{nome_janela}' com dimensões: ({left}, {top}, {right}, {bottom})")

    # Capturar a região da tela com base no bbox
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save(arquivo_screenshot)
    print(f"Screenshot completo salvo como: {arquivo_screenshot}")

    return arquivo_screenshot, (left, top, right, bottom)

def define_janela(nome_janela, arquivo_screenshot="janela_screenshot.png"):
    """
    Busca a janela pelo título, coloca-a em foco, obtém suas coordenadas (left, top, right, bottom)
    e então chama a função de captura de tela.
    """
    global left, top, right, bottom

    # Verificar se a janela existe
    janela = gw.getWindowsWithTitle(nome_janela)
    if not janela:
        print(f"Janela '{nome_janela}' não encontrada!")
        return False
    
    # Vamos pegar a primeira janela que corresponda ao título
    janela = janela[0]

    # Traz a janela para o topo
    hwnd = janela._hWnd
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    pyautogui.sleep(1)  # Tempo adicional para garantir foco

    print(f"Janela '{nome_janela}' trazida para o topo.")

    # Obter dimensões da janela
    # pygetwindow retorna:
    #   janela.left, janela.top, janela.width, janela.height
    left   = janela.left
    top    = janela.top
    width  = janela.width
    height = janela.height

    # O 'right' e 'bottom' devem ser calculados somando left+width e top+height
    right  = left + width
    bottom = top + height

    # Agora captura a janela usando essas coordenadas
    screenshot, coords = capturar_janela(arquivo_screenshot)
    if screenshot is None:
        print("Falha ao capturar a janela.")
        return False

    return True

def batalha():
    global leppa, pokes 
    #verificar se a batalha apenas 1 ou horda
    #se for 1, batalhar
    #se for horda, fugir
    imagem_caminho = "validador.png"
    imagem_botao   = "horda.png"

    # Carregar imagens com OpenCV
    imagem_principal = cv2.imread(imagem_caminho)
    img_botao        = cv2.imread(imagem_botao)
    
    # Verifica se as imagens foram carregadas
    if imagem_principal is None:
        print("Não foi possível carregar validador.png")
        return
    if img_botao is None:
        print("Não foi possível carregar horda.png")
        return
    
    # Localiza o 'barra de vida' na imagem principal
    resultado = cv2.matchTemplate(imagem_principal, img_botao, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Se o resultado é maior que 0.8, significa que é horda
    if max_val > 0.8:
        print("Encontrou horda!")
        print("Aguarde...")
        # mover mouse para posicao x = 1300 e y = 850  na janela
        pyautogui.moveTo(1450, 900)
        # Simula o clique do mouse
        pyautogui.click()
        time.sleep(6)        
        
        # Aqui você pode implemwentar a lógica do que fazer em batalha
    else:
        print("Encontrou batalha individual!")
        # mover mouse para posicao x = 1300 e y = 850 na janela
        
        pyautogui.moveTo(1300, 850)
       
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)        
        pyautogui.click()
        time.sleep(11)
        leppa += 1
        pokes += 1
        
def recarga_leppa_berry():
    global leppa, pokes 
    leppa -= 10
    pyautogui.moveTo(1615, 280)
    # Simula o clique do mouse
    pyautogui.click()
    
    pyautogui.moveTo(1650, 710)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.click()
    pyautogui.moveTo(1700, 796)
    time.sleep(1.5)
    pyautogui.click()
    time.sleep(3)

if __name__ == "__main__":
    # 1) Define a janela e captura a primeira imagem (validador.png)
    if define_janela(nome_janela, "validador.png"):
        # 2) Verifica se está em batalha (busca "battle.png" em "validador.png")
        while True:
            print(f'Número de leppa: {leppa}')
            print(f'Número de pokémon mortos: {pokes}')
            captura_batalha()
            if leppa == 10:
                recarga_leppa_berry()
            
            
                
        