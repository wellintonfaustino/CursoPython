# pip install --upgrade pip
# pip install --upgrade pyautogui pyscreeze pillow

# Exemplo de uso do pyautogui

import pyautogui

# Aguarda 3 segundos

pyautogui.sleep(3)

# Obtém a posição do mouse

mouse_x, mouse_y = pyautogui.position()

print(f'Mouse posicionado em: ({mouse_x}, {mouse_y})')

# Obtém a resolução da tela

resolution = pyautogui.size()

print(f'Resolução da tela: {resolution[0]}x{resolution[1]}')

# Obtém a cor do pixel na posição do mouse

color = pyautogui.pixel(mouse_x, mouse_y)

print(f'Cor do pixel: {color}')

# Clica no centro da tela

pyautogui.click(resolution[0] / 2, resolution[1] / 2)