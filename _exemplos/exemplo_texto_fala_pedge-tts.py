import edge_tts
import asyncio

async def gerar_audio():
    texto = "Você está panguándo"
    comunicador = edge_tts.Communicate(texto, voice="pt-BR-FranciscaNeural")
    await comunicador.save("audio.mp3")

asyncio.run(gerar_audio())
print("Áudio salvo como audio.mp3")
