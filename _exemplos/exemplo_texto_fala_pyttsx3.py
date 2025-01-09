# exemplo_texto_fala.py

import pyttsx3

# Inicializar o mecanismo de texto para fala
engine = pyttsx3.init()

# Texto a ser convertido em áudio
texto = "Este é um exemplo de conversão de texto para áudio usando Python com pyttsx3."

# Configurar propriedades da voz (opcional)
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 0.9)  # Volume (0.0 a 1.0)

# Converter texto em fala
engine.say(texto)

# Salvar o audio

engine.save_to_file(texto, "audio.mp3")

# Reproduzir o áudio
engine.runAndWait()
