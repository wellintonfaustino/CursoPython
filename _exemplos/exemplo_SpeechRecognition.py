# python exemplo_SpeechRecognition.py
# winget install "FFmpeg (Essentials Build)"
# path do windows: C:\Users\WELLIN~1.FAU\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-essentials_build\bin


import speech_recognition as sr

# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Carrega o arquivo de áudio
audio_file_path = "arquivo_convertido.wav"

with sr.AudioFile(audio_file_path) as source:
    # Lê o áudio do arquivo
    audio_data = recognizer.record(source)
    try:
        # Usa o Google Web Speech API para transcrever
        texto = recognizer.recognize_google(audio_data, language="pt-BR")  # Defina o idioma desejado
        print("Texto transcrito:")
        print(texto)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro na solicitação do serviço de reconhecimento: {e}")
