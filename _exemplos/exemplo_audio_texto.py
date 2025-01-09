import speech_recognition as sr

# Inicializar o reconhecedor
reconhecedor = sr.Recognizer()

# Carregar o arquivo de áudio
audio_file = "audio.wav"  # Certifique-se de usar um arquivo de áudio compatível (WAV ou compatível com PCM)

with sr.AudioFile(audio_file) as source:
    # Ajustar ruído ambiente (opcional)
    reconhecedor.adjust_for_ambient_noise(source)

    # Capturar o áudio
    audio = reconhecedor.record(source)

try:
    # Usar o serviço do Google para reconhecimento
    texto = reconhecedor.recognize_google(audio, language="pt-BR")
    print(f"Texto reconhecido: {texto}")
except sr.UnknownValueError:
    print("Não foi possível entender o áudio.")
except sr.RequestError as e:
    print(f"Erro ao se conectar ao serviço: {e}")
